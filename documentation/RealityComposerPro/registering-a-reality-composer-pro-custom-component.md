# Registering a Reality Composer Pro custom component

**Framework**: Reality Composer Pro

Expose a custom component to the Reality Composer Pro editor and RealityKit Scripting.

#### Overview

Reality Composer Pro’s built-in components cover common behavior, but your project’s own data — game state, gameplay parameters, or simulation values — doesn’t always map onto an existing component. You extend Reality Composer Pro by defining a custom component and registering it with Reality Composer Pro. The component then behaves like a built-in component in the editor and in the Inspector, and it becomes available to tools such as Script Graph’s Get Component, Set Component, and Has Component nodes.

This article walks through defining a custom `RotationComponent` (the same component used in `ExampleApp/ContentView.swift`) and then registering the component with Reality Composer Pro’s editor. After you register the component, designers can add and edit it visually. Registering it with RealityKit Scripting also lets JavaScript scripts running via `ScriptingComponent` read and write it.

![A diagram showing the overall process of registering a custom component with Reality Composer Pro.](/images/RealityComposerPro/ScriptGraphCustomComponentRegistrationWorkflow@2x.png)

#### Review the Reality Composer Pro Plugin Interface

The `RealityComposerPro` Swift package defines the plugin protocol Reality Composer Pro loads at runtime:

- **`RealityComposerProPlugin`**: Conform to this and implement `setup(context:)` to register your types. `shutdown()` is optional (default no-op).
- **`RealityComposerProContext`**: Passed into `setup(context:)`. It exposes: - `registerComponent<ComponentType: Component & Codable>(_:)`
- `registerComponent<ComponentType: Component & Codable>(_:defaultValue:)`
- `registerAction<ActionType: EntityAction>(_:)` (not used/out of scope for this article)
- `registerSystem(_:)`
- **`passRetained()`**: Boxes your plugin instance into an opaque pointer. Use `Unmanaged.passRetained(_:).toOpaque()` from the standard library, not a protocol member.
- **`@_cdecl("createRealityComposerProPlugin")`**: A free function marked with this attribute is the entry point Reality Composer Pro looks for when loading the plugin bundle.

`registerComponent` requires [`Component`](https://developer.apple.com/documentation/realitykit/component) and `Codable` — Reality Composer Pro needs to serialize your component into `.usda`/scene files, which `Inspectable` (RealityKit Scripting’s requirement) doesn’t provide by itself. A component destined for both worlds needs to conform to both.

#### Define the Custom Rotation Component

This mirrors the component from `ExampleApp/ContentView.swift`, with `Codable` added so you can also register it with Reality Composer Pro:

```swift
import RealityKit
import RealityKitScripting
public struct RotationComponent: Component, Codable {
    var rotationSpeed: Float
    var rotationAxis: SIMD3<Float> = .init(0, 1, 0)
    var isPaused: Bool = false
    // Wobble properties (exposed via extension in Overview.md's "Extending Existing Types")
    var wobbleEnabled: Bool = false
    var wobbleAmplitude: Float = 0.1
    var wobbleSpeed: Float = 5.0
    init(rotationSpeed: Float) {
        self.rotationSpeed = rotationSpeed
    }
}
extension RotationComponent: Inspectable {}
```

Give it a scripting schema, following the `static var schema` convention used throughout RealityKit Scripting (for example, `CoreComponent.schema` in the Hot Reload example):

```swift
extension RotationComponent {
    static var schema: TypeSchema<RotationComponent> {
        TypeSchema<RotationComponent>("RotationComponent") {
            Constructor(body: RotationComponent.init(rotationSpeed:))
            StoredProperty("rotationSpeed", keyPath: \RotationComponent.rotationSpeed)
            StoredProperty("rotationAxis", keyPath: \RotationComponent.rotationAxis)
            StoredProperty("isPaused", keyPath: \RotationComponent.isPaused)
            StoredProperty("wobbleEnabled", keyPath: \RotationComponent.wobbleEnabled)
            StoredProperty("wobbleAmplitude", keyPath: \RotationComponent.wobbleAmplitude)
            StoredProperty("wobbleSpeed", keyPath: \RotationComponent.wobbleSpeed)
        }
    }
}
```

> 💡 **Tip**: The `@Scriptable` macro generates the `Inspectable` conformance and the schema for you. The macro replaces the extension and static var schema block in the code sample above. Add `import RealityKitScriptingMacros`, annotate the type with `@Scriptable`, and mark the members you want to expose as public. The macro only exposes public members, or ones annotated with `@Visible`. You access generated schemas as `RotationComponent.SchemaProvider.schema` rather than `RotationComponent.schema`. See the following example:

```swift
import RealityKit
import RealityKitScripting
import RealityKitScriptingMacros

@Scriptable
public struct RotationComponent: Component, Codable {
    public var rotationSpeed: Float
    public var rotationAxis: SIMD3<Float> = .init(0, 1, 0)
    public var isPaused: Bool = false
    public var wobbleEnabled: Bool = false
    public var wobbleAmplitude: Float = 0.1
    public var wobbleSpeed: Float = 5.0

    public init(rotationSpeed: Float) {
        self.rotationSpeed = rotationSpeed
    }
}
```

#### Register the Custom Component with the Plugin

Implement `RealityComposerProPlugin` and register the component twice in `setup(context:)`: once with the Reality Composer Pro `context` (editor support), and once with `ScriptingRuntime` (RealityKit Scripting, for scripting support). In the following example, `RotationComponent.schema` refers to the manually-defined schema. If you use `@Scriptable` (shown in the previous section), substitute `RotationComponent.SchemaProvider.schema`.

```swift
import RealityComposerPro
import RealityKitScripting
final class RotationPlugin: RealityComposerProPlugin {
    func setup(context: any RealityComposerProContext) {
        // 1. Register with Reality Composer Pro so designers can add/edit
        //    RotationComponent in the Reality Composer Pro Inspector, and
        //    so it round-trips through .usda/.reality scene files.
        context.registerComponent(RotationComponent.self, defaultValue: RotationComponent(rotationSpeed: 1))
        // 2. Register with RealityKitScripting so scripts (via ScriptingComponent)
        //    can read/write RotationComponent at runtime.
        let scriptingConfig = ScriptingRuntime.Configuration { _ in
            let module = Module("RotationPlugin") {
                RotationComponent.schema
            }
            return [module]
        }
        do {
            try ScriptingRuntime.addConfiguration(scriptingConfig)
        } catch {
            assertionFailure("Failed to add RealityKitScripting configuration: \(error)")
        }
    }
}
@_cdecl("createRealityComposerProPlugin")
public func createRealityComposerProPlugin() -> UnsafeMutableRawPointer {
    Unmanaged.passRetained(RotationPlugin()).toOpaque()
}
```

`ScriptingRuntime.addConfiguration` initializes `ScriptingRuntime` if needed and reloads immediately, so the schema is available as soon as the plugin loads — no separate startup step required.

#### Compare What Each Registration Provides

The two registration calls serve different audiences and run at different times. See the following comparison.

| Description | `registerComponent` | `addConfiguration` |
| --- | --- | --- |
| **Purpose** | Exposes component to Reality Composer Pro | Exposes component to RealityKit Scripting (JavaScript via `ScriptingComponent`) |
| **Who uses it** | Designers (scene authoring) | Developers writing JavaScript scripts, at runtime |
| **What it enables** | Component appears in picker/Inspector; properties editable visually; saved into scene file | `entity.getComponent(...)` read/write access from JavaScript |
| **When it runs** | Edit time | Runtime |
| **Underlying type** | `RotationComponent` | `RotationComponent` (same) |

> **Note**: Both registrations point at the *same* `RotationComponent` storage — they are two faces of the same RealityKit component: one for scene editing, one for JavaScript scripting at runtime.

## See Also

- [Getting started with Script Graphs](getting-started-with-script-graphs.md)
  Build interactive, code-free 3D experiences using a visual, node-based editor in Reality Composer Pro.
- [Building custom interactive behavior with Script Graph](building-custom-interactive-behavior-with-script-graph.md)
  Build event-driven behavior with Script Graph with nodes, events, and components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/registering-a-reality-composer-pro-custom-component)*