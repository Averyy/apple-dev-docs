# MatchedGeometryProperties

**Framework**: SwiftUI  
**Kind**: struct

A set of view properties that may be synchronized between views using the `View.matchedGeometryEffect()` function.

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
struct MatchedGeometryProperties
```

## Topics

### Matching properties
- [static let frame: MatchedGeometryProperties](matchedgeometryproperties/frame.md)
  Both the `position` and `size` properties.
- [static let position: MatchedGeometryProperties](matchedgeometryproperties/position.md)
  The view’s position, in window coordinates.
- [static let size: MatchedGeometryProperties](matchedgeometryproperties/size.md)
  The view’s size, in local coordinates.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](view/matchedgeometryeffect(id:in:properties:anchor:issource:).md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [protocol GeometryEffect](geometryeffect.md)
  An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [struct Namespace](namespace.md)
  A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [func geometryGroup() -> some View](view/geometrygroup.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/matchedgeometryproperties)*