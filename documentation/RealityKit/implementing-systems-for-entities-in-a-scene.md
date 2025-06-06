# Implementing systems for entities in a scene

**Framework**: RealityKit

Apply behaviors and physical effects to the objects and characters in a RealityKit scene with the Entity Component System (ECS).

#### Overview

You can use RealityKit’s Entity Component System (ECS) to define and apply logic for entities in a scene. Systems are especially useful for implementing behavior that affects multiple entities in your scene, like the flocking behavior for a swarm of entities representing birds. In a traditional object-oriented approach, you implement an entity’s behavior by writing code on the entity class, which runs on every instance of that class on every update. That approach can be inefficient for scene with many entities, because RealityKit calls each entity’s update method on every rendering engine tick. That is especially true if the logic for one entity depends on a state contained in other entities.

With systems, RealityKit calls only one update method as often as defined by the `updatingSystemWhen` parameter of [`entities(matching:updatingSystemWhen:)`](sceneupdatecontext/entities(matching:updatingsystemwhen:).md), rather than calling an update method every scene update for each entity. A system iterates through all relevant entities every scene update and makes updates to their state as needed. Here’s how to implement your own systems.

##### Create a System Class

Create a system by a creating a class that conforms to the [`System`](system.md) protocol and implements two methods: [`init(scene:)`](system/init(scene:).md) and [`update(context:)`](system/update(context:).md). Perform the setup for your system in [`init(scene:)`](system/init(scene:).md), or add an empty implementation if your system doesn’t need any setup. Add the logic needed to run your system in [`update(context:)`](system/update(context:).md), which RealityKit calls every frame automatically.

```swift
class MySystem: System {
    required init(scene: Scene) { 
        // Perform required initialization or setup.
    }

    func update(context: SceneUpdateContext) {
        // RealityKit automatically calls this on
        // every update for every scene.
    }
}
```

> ⚠️ **Warning**: Don’t do any unnecessary work in the `update` method, as it is called very frequently. If your [`update(context:)`](system/update(context:).md) method takes a long time to return, it can negatively impact your app’s frame rate.

Don’t do any unnecessary work in the `update` method, as it is called very frequently. If your [`update(context:)`](system/update(context:).md) method takes a long time to return, it can negatively impact your app’s frame rate.

##### Retrieve Entities with an Entity Query

To efficiently retrieve entities from a scene, use an [`EntityQuery`](entityquery.md), which you can use to fetch all entities, or just a subset of entities relevant to your system. While some systems operate on every entity in the scene, most only operate on a defined subset, often based on the entities’ components. A physics simulation system, for example, only needs to operate on entities that participate in the scene’s physics simulation and a rendering system only needs to operate on entities that are visible. To retrieve a subset of your scene’s entities, create a [`QueryPredicate`](querypredicate.md) with your criteria and pass the predicate into the initializer when creating your entity query.

Create your query as a static property of your system unless your query criteria changes between update calls. If the criteria changes between update calls, create the query in your update method. Use the entity query with [`entities(matching:updatingSystemWhen:)`](sceneupdatecontext/entities(matching:updatingsystemwhen:).md) in your [`update(context:)`](system/update(context:).md) method to iterate over all the entities that your system depends on.

```swift
struct MyComponent: Component {
    // Optionally, put any needed state here.
}

class MySystem: System {

    // Define a query to return all entities with a MyComponent.
    private static let query = EntityQuery(where: .has(MyComponent.self))

    // Initializer is required. Use an empty implementation if there's no setup needed.
    required init(scene: Scene) { }

    // Iterate through all entities containing a MyComponent.
    func update(context: SceneUpdateContext) {
        for entity in context.entities(
            matching: Self.query,
            updatingSystemWhen: .rendering
        ) {
            // Make per-update changes to each entity here.
        }
    }
}
```

##### Create and Add Components in Reality Composer Pro

If you use a Reality Composer Pro package in your project, you can create new components within the editor by selecting an entity, clicking the Add Component button, and then selecting the New Component option. This creates a Swift template for the new component, which you can then edit in Xcode.

To add a custom component onto an entity, define the custom component in a file in your Reality Composer Pro package. Select the entity you want to add the custom component to, click the Add Component button, then select the name of your custom component. This entity then responds and behaves according to the same systems that you wrote to query for the custom component.

##### Specify System Dependencies

If a system relies on another system to function, or if you need to specify the update order for multiple systems, declare a [`dependencies`](system/dependencies.md) array in your system. To tell RealityKit that a dependency must update before your system, use the [`SystemDependency.before(_:)`](systemdependency/before(_:).md) enumeration case, passing the other system as a parameter. For dependencies that must update after your system, use [`SystemDependency.after(_:)`](systemdependency/after(_:).md), instead.

```swift
class SystemB: RealityKit.System {
    static var dependencies: [SystemDependency] { 
        [.after(SystemA.self),        // Run SystemB after SystemA.
         .before(SystemC.self)]       // Run SystemB before SystemC.
     }
    // ... 
}
```

##### Register the System

You don’t create [`System`](system.md) instances manually. RealityKit creates them for you, but only if you tell RealityKit about your system by calling its [`registerSystem()`](system/registersystem().md) method before displaying your app’s [`ARView`](arview.md). Once you’ve registered your system, RealityKit automatically creates an instance on your system for every active scene, then repeatedly calls its [`update(context:)`](system/update(context:).md) method every scene update.

```swift
MySystem.registerSystem()
```

## See Also

- [protocol System](system.md)
  An object that affects multiple entities in every update of a RealityKit scene.
- [struct SystemUpdateCondition](systemupdatecondition.md)
  A condition which causes a system to update.
- [struct SceneUpdateContext](sceneupdatecontext.md)
  An object that contains information about the scene to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/implementing-systems-for-entities-in-a-scene)*