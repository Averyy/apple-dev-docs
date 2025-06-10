# has(_:)

**Framework**: RealityKit  
**Kind**: method

Creates a new predicate that describes entities that have a specific component.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static func has<T>(_ t: T.Type) -> QueryPredicate<Entity> where T : Component
```

#### Return Value

A predicate that describes entities with a specified component.

#### Discussion

To create a `has` predicate, pass the component class’s `self` property.

```swift
let myPredicate = QueryPredicate.has(ModelComponent.self)
```

## Parameters

- `t`: The type of component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/querypredicate/has(_:))*