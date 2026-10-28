# Anchor.Source

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

SwiftUI passes anchored geometry values around the view tree via preference keys. It then converts them back into the local coordinate space using a [`GeometryProxy`](../geometryproxy.md) value.

## Topics

### Getting point anchor sources
- [static point(_:)](./source/point%28_%29.md)
- [static unitPoint(_:)](./source/unitpoint%28_%29.md)
### Getting rectangle anchor sources
- [static func rect(CGRect) -> Anchor<Value>.Source](./source/rect%28_%29.md)
  Returns an anchor source rect defined by `r` in the current view.
- [static var bounds: Anchor<CGRect>.Source](./source/bounds.md)
  An anchor source rect defined as the entire bounding rect of the current view.
### Getting top anchor sources
- [static var topLeading: Anchor<CGPoint>.Source](./source/topleading.md)
- [static var top: Anchor<CGPoint>.Source](./source/top.md)
- [static var topTrailing: Anchor<CGPoint>.Source](./source/toptrailing.md)
### Getting middle anchor sources
- [static var leading: Anchor<CGPoint>.Source](./source/leading.md)
- [static var center: Anchor<CGPoint>.Source](./source/center-869al.md)
- [static var trailing: Anchor<CGPoint>.Source](./source/trailing.md)
### Getting bottom anchor sources
- [static var bottomTrailing: Anchor<CGPoint>.Source](./source/bottomtrailing.md)
- [static var bottom: Anchor<CGPoint>.Source](./source/bottom.md)
- [static var bottomLeading: Anchor<CGPoint>.Source](./source/bottomleading.md)
### Creating an anchor source
- [init(_:)](./source/init%28_%29.md)
### Type Properties
- [static var bounds3D: Anchor<Rect3D>.Source](./source/bounds3d.md)
  An anchor source rect defined as the entire bounding rect of the current element.
- [static var center: Anchor<Point3D>.Source](./source/center-6w6ww.md)
- [static var center3D: Anchor<Point3D>.Source](./source/center3d.md)
### Type Methods
- [static func point3D(Point3D) -> Anchor<Value>.Source](./source/point3d%28_%29.md)
- [static func rect3D(Rect3D) -> Anchor<Value>.Source](./source/rect3d%28_%29.md)
  Returns an anchor source rect defined by `r` in the current element.
- [static func unitPoint3D(UnitPoint3D) -> Anchor<Value>.Source](./source/unitpoint3d%28_%29.md)

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anchor/source)*