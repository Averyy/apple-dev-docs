# Anchor.Source

**Framework**: SwiftUI  
**Kind**: struct

A type-erased geometry value that produces an anchored value of a given type.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct Source
```

#### Overview

SwiftUI passes anchored geometry values around the view tree via preference keys. It then converts them back into the local coordinate space using a [`GeometryProxy`](geometryproxy.md) value.

## Topics

### Getting point anchor sources
- [static point(_:)](anchor/source/point(_:).md)
- [static unitPoint(_:)](anchor/source/unitpoint(_:).md)
### Getting rectangle anchor sources
- [static func rect(CGRect) -> Anchor<Value>.Source](anchor/source/rect(_:).md)
  Returns an anchor source rect defined by `r` in the current view.
- [static var bounds: Anchor<CGRect>.Source](anchor/source/bounds.md)
  An anchor source rect defined as the entire bounding rect of the current view.
### Getting top anchor sources
- [static var topLeading: Anchor<CGPoint>.Source](anchor/source/topleading.md)
- [static var top: Anchor<CGPoint>.Source](anchor/source/top.md)
- [static var topTrailing: Anchor<CGPoint>.Source](anchor/source/toptrailing.md)
### Getting middle anchor sources
- [static var leading: Anchor<CGPoint>.Source](anchor/source/leading.md)
- [static var center: Anchor<CGPoint>.Source](anchor/source/center-869al.md)
- [static var trailing: Anchor<CGPoint>.Source](anchor/source/trailing.md)
### Getting bottom anchor sources
- [static var bottomTrailing: Anchor<CGPoint>.Source](anchor/source/bottomtrailing.md)
- [static var bottom: Anchor<CGPoint>.Source](anchor/source/bottom.md)
- [static var bottomLeading: Anchor<CGPoint>.Source](anchor/source/bottomleading.md)
### Creating an anchor source
- [init(_:)](anchor/source/init(_:).md)
### Type Properties
- [static var bounds3D: Anchor<Rect3D>.Source](anchor/source/bounds3d.md)
  An anchor source rect defined as the entire bounding rect of the current element.
- [static var center: Anchor<Point3D>.Source](anchor/source/center-6w6ww.md)
- [static var center3D: Anchor<Point3D>.Source](anchor/source/center3d.md)
### Type Methods
- [static func point3D(Point3D) -> Anchor<Value>.Source](anchor/source/point3d(_:).md)
- [static func rect3D(Rect3D) -> Anchor<Value>.Source](anchor/source/rect3d(_:).md)
  Returns an anchor source rect defined by `r` in the current element.
- [static func unitPoint3D(UnitPoint3D) -> Anchor<Value>.Source](anchor/source/unitpoint3d(_:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anchor/source)*