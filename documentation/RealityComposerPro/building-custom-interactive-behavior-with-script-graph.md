# Building custom interactive behavior with Script Graph

**Framework**: Reality Composer Pro

Build event-driven behavior with Script Graph with nodes, events, and components.

#### Overview

Script Graph is the node-based tool in Reality Composer Pro for authoring interactive behavior on an entity, which is the RealityKit object that carries components and appears in your scene. A Script Graph produces a scripting component that ships with your app and runs as part of the scene. Script Graph is for creating runtime behavior rather than programmatic editor workflows. You open a graph from an entity’s Scripting component or from a Script Graph asset in the Project Browser. This will open the Graph tab, the same node-editing surface that Reality Composer Pro also uses for Shader Graphs, Animation Graphs, and Compute Graphs.

Unlike Shader Graphs, Script Graph is event-driven. A graph starts running at one or more event nodes, such as Update, a collision event, or a tap. The graph runs and then flows outward along edges to other nodes, carrying data values and dictating the order operations run in. Alongside typed data ports, Script Graph nodes also expose graph event ports for sequencing. These ports are drawn as small plungers next to the node header. Event ports are what separate Script Graph from a Shader Graph.

The built-in node library covers a wide range of node categories; for example, Entity-related nodes or component manipulation nodes. You can extend the existing node library by binding your own components via a Reality Composer Pro Plugin, which allows Script Graph to access your custom component. This enables you to use the same generic nodes as for the RealityKit built-in components. To learn how to define a custom component and register it with Reality Composer Pro — see [`Registering a Reality Composer Pro custom component`](registering-a-reality-composer-pro-custom-component.md).

This article walks through building behavior inside the Script Graph Editor — wiring nodes, working with events, and reading and writing components, including your own.

#### Open the Script Graph Editor for an Entity

Open an entity’s Scripting component as described in [`Getting started with Script Graphs`](getting-started-with-script-graphs.md), then double-click it to open its graph in the Graph tab.

> 💡 **Tip**: Because the Graph tab hosts several graph types, make sure you’re in the right one: a Script Graph shows graph event ports (the plunger-shaped pins next to a node’s header) that a Shader Graph never displays.

#### Choose Between Variables and Inputs

Script Graphs expose two ways to pass data into your logic: Variables and Inputs. Configure Script Graph variables and Inputs in the Inspector.

Variables are named, typed values that persist and can change at runtime. Variables can store any data the graph supports. Variable scope is controlled by the **Internal Accessible** flag, which determines whether subgraphs and external graphs can access them. If a variable is marked **Internal Accessible,** any subgraphs of the parent graph automatically have read and write access to it.

> **Note**: Internal Accessible controls the visibility boundary of a variable. Turning it on is the same as making a property `internal` or `public` — it widens scope from the defining graph outward to subgraphs and external consumers.

Other graphs can also reference the variable externally through a reference to the entity and the variable. Otherwise, only the graph that defines the variable can access it.

> 💡 **Tip**: Use a Script Graph variable when you need values that can change during runtime, such as a health value a component reads and a Set Component node writes back after each hit.

![A screenshot of the Reality Composer Pro Inspector showing the Script Graph Variable section.](/images/RealityComposerPro/ScriptGraphInspectorView@2x.png)

Inputs are values passed directly into a graph or subgraph at the point of invocation. They are best suited for one-time or per-call data rather than persistent state.

> 💡 **Tip**: Use Inputs instead of variables when you want to reuse your graph as a subgraph. For example, one component’s data configuring the strength or color of an effect each time the subgraph runs.

#### Wire Nodes with Graph Event Ports

Alongside the typed data ports covered in [`Getting started with Script Graphs`](getting-started-with-script-graphs.md), Script Graph nodes expose graph event ports for sequencing. Event ports are drawn as small plungers next to the node header. Graph event output ports follow the same one-connection rule as data ports, unless the specific node type says otherwise; for the general wiring rules that apply to any port type, see [`Getting started with Script Graphs`](getting-started-with-script-graphs.md). Some nodes, such as Sequence, And, and Or, expose a dynamic port marked `(+)` at the end of their existing ports. Dropping a valid connection on it adds a new port in its place, which is how those nodes grow to accept more inputs than they started with.

#### Start a Graph From an Event Node

A Script Graph does nothing until it is started with an event node, such as a frame update, a collision, an input like a tap, or an entity lifecycle event. Wire an event node’s graph event output into the rest of your graph, and everything downstream runs in the order your edges describe. A Script Graph runs based on events, and it starts and stops along with the component or entity it belongs to. The following Lifecycle Event nodes control when your graph starts and stops. Choosing the right node helps your graph avoid stale subscriptions, unexpected re-runs, and resource leaks.

![A diagram showing how Reality Composer Pro Script Graph Nodes map to RealityKit nodes.](/images/RealityComposerPro/ScriptGraphComponentNodeMap@2x.png)

The Lifecycle Event nodes are as follows:

| Node | Timing | Frequency | Trigger Condition | RealityKit Event | API Ref |
| --- | --- | --- | --- | --- | --- |
| **On Update** | During frame | Every frame | Component is modified each frame | `ComponentEvents.DidChange` | [`API`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/componentevents/didchange) |
| **On Initialize** | After first add | Once | Component is first added to an entity | *(no direct RealityKit event)* | — |
| **On Add** | After add | Per add | Component added to entity, including re-adds after removal from scene | `ComponentEvents.DidAdd` | [`API`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/componentevents/didadd) |
| **On Activate** | After activation | Per activation | Entity becomes active | `ComponentEvents.DidActivate` | [`API`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/componentevents/didactivate) |
| **On Remove** | Before removal | Per removal | Just before RealityKit removes the component from an entity | `ComponentEvents.WillRemove` | [`API`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/componentevents/willremove) |
| **On Deactivate** | Before deactivation | Per deactivation | Just before entity or component deactivates | `ComponentEvents.WillDeactivate` | [`API`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/componentevents/willdeactivate) |

> **Note**: **Note:** **On Add** and **On Initialize** differ in one key way: On Initialize fires only once (first add), while On Add fires on every add — including re-adds after the entity was removed from the scene, even without a prior initialization. See [`Reality Kit Component Events`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/componentevents) for more information.

![A diagram showing entity lifecycles for different use cases.](/images/RealityComposerPro/ScriptGraphEntityLifecycle@2x.png)

#### Send and Subscribe to Events From a Script Graph

To send and subscribe to events in a custom plugin, you will need to add code to where you register the components and system.

##### Example Sending Scene Events

```swift
scene.send(name: "scoreChanged", arguments: ["score": 42])
```

Any script (or Swift subscriber) listening for `"scoreChanged"` on that scene receives the event. `ScriptingEvent.arguments` are automatically converted to/from JavaScript-compatible types.

##### Example Subscribing to Scene Events

```swift
let subscription = scene.subscribe(to: "scoreChanged") { event in
    print("Score changed:", event.arguments)
}
// Keep a strong reference (e.g. in a Set<AnyCancellable> or [AnyCancellable])
// so the subscription isn't torn down immediately.
subscription.store(in: &subscriptions)

```

##### Example Subscribing to Entity Events

Events can also target a specific `Entity`. The entity must carry a `ScriptingComponent` to subscribe or receive entity-targeted events.

```swift
let subscription = entity.subscribe(to: "hit") { event in
    print("Entity was hit:", event.arguments)
}
subscription?.store(in: &subscriptions)
```

`subscribe(to:_:)` returns `nil` if the entity isn’t attached to a scene yet, or doesn’t have a `ScriptingComponent`. The subscription is also cancelled automatically if the `ScriptingComponent` is removed/replaced or the entity is discarded.

#### Decouple Behavior with a Custom Event

Chaining every reaction directly off a single event node works for small graphs, but it gets unwieldy once several unrelated things need to happen in response to the same condition. Custom Event Node solves this by defining a named entry point that other parts of your graph — or another graph or subgraph entirely — can invoke without knowing anything about how it’s implemented internally. To fire a custom event, use a Scene or Entity Event Node, which raises the named event so any Custom Event Node listening for it starts running. Any graph with an On Scene Event node can listen for a Scene Event. Only the specifically targeted entity’s On Entity Node can listen for an Entity Event. This pairing is a natural fit once you introduce your own component data from Swift: rather than having a branch of your graph poll a component’s value every frame, you can have the branch that changes the value also trigger a custom event, letting the rest of the graph react only when something actually changes.

#### Extend Behavior with a Custom Component

At some point the built-in node library won’t cover what your project needs — maybe you have game state, gameplay parameters, or simulation data that doesn’t map cleanly onto an existing component. Script Graph doesn’t let you author new node types, and it doesn’t support custom port data types. It offers a fixed set: booleans, numbers, strings, the `Float` and matrix types, [`CGColor`](https://developer.apple.com/documentation/coregraphics/cgcolor), doc://com.apple.documentation/documentation/coregraphics/CGPoint, doc://com.apple.documentation/documentation/coregraphics/CGSize, entities, scenes, and component values. What it does support is wrapping your data in a Custom Component: a Swift struct you register with Reality Composer Pro so it shows up in the editor exactly like a built-in component, including in the same Get Component, Set Component, and Has Component nodes.

> 💡 **Tip**: Register custom components by integrating RealityKit Scripting into your project. Otherwise, the custom components don’t appear in Reality Composer Pro. See [`RealityKit Scripting`](https://developer.apple.comhttps://github.com/apple/realitykitscripting) and [`RealityKit Scripting - Expose Custom Types`](https://developer.apple.comhttps://github.com/apple/realitykitscripting#4-expose-custom-types) for more information.

This is a whole-component exchange, not a field-by-field one — a Get Component node returns the entire struct, and a Set Component node writes the entire struct back. If you need a script to act on individual pieces of your data, read the component, inspect or modify the relevant fields inline in the graph, and write the whole component back rather than expecting each property to appear as its own port. See [`Reality Kit Scripting`](https://developer.apple.comhttps://github.com/apple/realitykitscripting/blob/main/overview.md) for more information and examples. To make your own Swift data available this way, define a custom component and register it with Reality Composer Pro through a plugin, as described in [`Registering a Reality Composer Pro custom component`](registering-a-reality-composer-pro-custom-component.md).

#### Read and Write the Custom Component in Script Graph

With the plugin loaded, your custom component behaves like any other component in the editor. Right-click the entity you want to carry the component’s data, choose Add Component, and pick it from the Custom Component submenu — only components successfully imported into the Custom Components folder appear there. Once added, you can edit its properties directly in the Inspector panel, the same way you’d edit a built-in component’s fields. Back in the Script Graph, the Components category’s Get Component, Set Component, and Has Component nodes now work against your custom type as a selectable option, the same way they work against any built-in component.

#### Run the Script in Your App at Runtime

To get your custom behavior into your app, export the entity — or a scene containing it — from the Project Browser as a `.reality` file, and make sure you include the entity with the Scripting component in the export. When your Xcode app loads that file as a RealityKit scene, the graph itself comes along as part of the entity’s data, but it won’t run on its own: the app also needs the RealityKit Scripting Swift package, which provides the scripting system responsible for executing Script Graph behavior at runtime. Without it, the exported entity loads normally, but its script never starts.

Any custom system you registered earlier keeps running once the app ships, exactly as it did in the Reality Composer Pro Simulate tab, processing entities that carry your custom component on every frame. Your Swift system can update a custom component’s data based on app-level logic, and any Script Graph reading that component — through Get Component, Has Component, or a custom event triggered when the value changes — sees the update as soon as it happens. You never need to leave RealityKit’s own component and system model to make the two sides talk to each other, as shown in the [`RealityKit Scripting sample’s script-attachment example`](https://developer.apple.comhttps://github.com/apple/realitykitscripting#3-attach-a-script).

## See Also

- [Getting started with Script Graphs](getting-started-with-script-graphs.md)
  Build interactive, code-free 3D experiences using a visual, node-based editor in Reality Composer Pro.
- [Registering a Reality Composer Pro custom component](registering-a-reality-composer-pro-custom-component.md)
  Expose a custom component to the Reality Composer Pro editor and RealityKit Scripting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-custom-interactive-behavior-with-script-graph)*