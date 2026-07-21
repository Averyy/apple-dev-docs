# set(qualifiedComponentName:representation:)

**Framework**: RealityKit  
**Kind**: method

Adds component data to an entity that is written to a Reality file but has no other effect at author time.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func set(qualifiedComponentName: String, representation: some Encodable) throws
```

#### Discussion

Use this function from an authoring tool to serialize a component whose Swift type isn’t available on the authoring platform. `representation` is encoded into any Reality file this entity is written to, and is decoded back into a [`Component`](component.md) of the type named by `qualifiedComponentName` when that file is loaded, so it must encode to the layout that component expects. For runtime use on a platform where the component’s Swift type is available, set the component directly with `set(_:)` instead.

```swift
// Serialize a custom component by its fully qualified name.
struct MyCustomComponent: Component, Codable {
    var intensity: Float
}
try entity.components.set(
    qualifiedComponentName: "MyModule.MyCustomComponent",
    representation: MyCustomComponent(intensity: 0.5))
```

> **Note**: An error if `representation` can’t be encoded, or if `qualifiedComponentName` uses a reserved prefix.

## Parameters

- `qualifiedComponentName`: The component’s fully qualified, module-qualified name.
- `representation`: A value that encodes to the component’s expected layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/componentset/set(qualifiedcomponentname:representation:))*