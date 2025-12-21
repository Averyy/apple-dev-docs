# QueryPredicate

**Framework**: RealityKit  
**Kind**: struct

An object that defines the criteria for an entity query.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct QueryPredicate<Value>
```

## Mentions

- [Implementing systems for entities in a scene](implementing-systems-for-entities-in-a-scene.md)

#### Overview

Query predicates specify the entities an [`EntityQuery`](entityquery.md) returns from a scene. Predicates describe entities based on which components they contain, or on the entity’s relationship to other entities in the scene. For example, you can build a predicate to retrieve the model entities from a scene.

```swift
let modelPredicate = QueryPredicate.has(ModelComponent.self)
```

##### Create Compound Predicates

You can combine predicates using Swift’s logical operators to create compound predicates. [`QueryPredicate`](querypredicate.md) supports Swift’s logical `AND` (`&&`), logical `OR` (`||`), and logical `NOT` (`!`) operators. The following code shows how to build a compound predicate that returns all entities that are either model entities or anchor entities:

```swift
let orPredicate: QueryPredicate<Entity> =
    .has(ModelComponent.self) || .has(AnchorComponent.self)
```

Use parentheses to control the order of operations when combining predicates. For example, you can create a query that returns any entity that has both a model component and a physics body component, or any entity that has only an anchor component.

```swift
let multiPredicate: QueryPredicate<Entity> =
    .has(ModelComponent.self) && .has(PhysicsBodyComponent.self) ||
    .has(AnchorComponent.self)
```

## Topics

### Creating predicates
- [static func has<T>(T.Type) -> QueryPredicate<Entity>](querypredicate/has(_:).md)
  Creates a new predicate that describes entities that have a specific component.
### Comparing predicates
- [func ! <Value>(QueryPredicate<Value>) -> QueryPredicate<Value>](!(_:).md)
  Returns a predicate which evaluates to `true` if `operand` evaluates to `false`.
- [func && <Value>(QueryPredicate<Value>, QueryPredicate<Value>) -> QueryPredicate<Value>](&&(_:_:).md)
  Returns a predicate which evaluates to `true` if `left` AND `right` evaluate to `true`.
- [func || <Value>(QueryPredicate<Value>, QueryPredicate<Value>) -> QueryPredicate<Value>](__(_:_:).md)
  Returns a predicate which evaluates to `true` if `left` OR `right` evaluates to `true`.

## See Also

- [struct PixelCastHit](pixelcasthit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/querypredicate)*