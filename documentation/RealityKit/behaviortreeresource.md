# BehaviorTreeResource

**Framework**: RealityKit  
**Kind**: class

An immutable representation of a behavior tree.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class BehaviorTreeResource
```

#### Overview

A `BehaviorTreeResource` can be produced by compiling a tree definition. Once compiled, assign it to an entity via [`BehaviorTreeComponent`](behaviortreecomponent.md) to begin driving behaviors:

let treeResource1 = try BehaviorTreeResource(definition: Data(behaviorTreeDefinition1.utf8)) let treeResource2 = try BehaviorTreeResource(definition: Data(behaviorTreeDefinition2.utf8)) let treeResources: [String : BehaviorTreeResource] = [“tree1” : treeResource1, “tree2” : treeResource2] entity.components.set(BehaviorTreeComponent(behaviorTree: resource, availableBehaviorTrees: treeResources))

#### Parameters

The tree exposes a set of named parameters that control its behavior at runtime, such as movement speed. Read the available parameters via [`parameterNames`](behaviortreeresource/parameternames.md). To set values at runtime, use the entity’s parameter binding:

entity.parameters[“MoveSpeed”] = BindableValue(Float(1.0))

## Topics

### Creating a behavior tree
- [convenience init(definition: Data) throws](behaviortreeresource/init(definition:).md)
  Compile a new resource from data, throws on failure.
### Validating a definition
- [static func validate(definition: Data) -> [String]](behaviortreeresource/validate(definition:).md)
  Run the compiler and return all tree errors without producing a resource.
### Accessing parameters
- [var parameterNames: [String]](behaviortreeresource/parameternames.md)
  Returns the names of all parameters in the behavior tree resource.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct BehaviorTreeComponent](behaviortreecomponent.md)
- [protocol BehaviorTreeAction](behaviortreeaction.md)
- [protocol BehaviorTreeActionHandler](behaviortreeactionhandler.md)
- [enum ActionResult](actionresult.md)
  Status values that an action can report back to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/behaviortreeresource)*