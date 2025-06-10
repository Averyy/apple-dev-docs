# Namespace

**Framework**: SwiftUI  
**Kind**: struct

A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
@propertyWrapper struct Namespace
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

## Topics

### Creating a namespace
- [init()](namespace/init.md)
### Getting the namespace
- [var wrappedValue: Namespace.ID](namespace/wrappedvalue.md)
- [Namespace.ID](namespace/id.md)
  A namespace defined by the persistent identity of an `@Namespace` dynamic property.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [DynamicProperty](dynamicproperty.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](view/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [struct MatchedGeometryProperties](matchedgeometryproperties.md)
  A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.
- [protocol GeometryEffect](geometryeffect.md)
  An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [func geometryGroup() -> some View](view/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/namespace)*