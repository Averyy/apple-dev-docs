# MatchedGeometryProperties

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static let frame: MatchedGeometryProperties](./matchedgeometryproperties/frame.md)
  Both the `position` and `size` properties.
- [static let position: MatchedGeometryProperties](./matchedgeometryproperties/position.md)
  The view’s position, in window coordinates.
- [static let size: MatchedGeometryProperties](./matchedgeometryproperties/size.md)
  The view’s size, in local coordinates.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Synchronizing geometries
- [func matchedGeometryEffect<ID>(id: ID, in: Namespace.ID, properties: MatchedGeometryProperties, anchor: UnitPoint, isSource: Bool) -> some View](./view/matchedgeometryeffect%28id,in,properties,anchor,issource%29.md)
  Defines a group of views with synchronized geometry using an identifier and namespace that you provide.
- [protocol GeometryEffect](./geometryeffect.md)
  An effect that changes the visual appearance of a view, largely without changing its ancestors or descendants.
- [struct Namespace](./namespace.md)
  A dynamic property type that allows access to a namespace defined by the persistent identity of the object containing the property (e.g. a view).
- [func geometryGroup() -> some View](./view/geometrygroup%28%29.md)
  Isolates the geometry (e.g. position and size) of the view from its parent view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/matchedgeometryproperties)*