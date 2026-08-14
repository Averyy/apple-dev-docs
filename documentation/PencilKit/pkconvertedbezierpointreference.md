# PKConvertedBezierPointReference

**Framework**: PencilKit  
**Kind**: class

An object that provides information about a B-spline control point converted from a Bézier path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class PKConvertedBezierPointReference
```

#### Overview

`PKConvertedBezierPointReference` is passed to the `pointProvider` block of `PKStrokePathReference/initWithBezierPath:creationDate:pointProvider:` so you can initialize each `PKStrokePoint` of the resulting path with appropriate values. A single instance is reused for each point in the conversion.

In Swift, use the equivalent value type [`PKStrokePath.ConvertedBezierPoint`](pkstrokepath-swift.struct/convertedbezierpoint.md) instead.

## Topics

### Getting the point data
- [var index: Int](pkconvertedbezierpointreference/index.md)
  The index of the point along the path.
- [var pointCount: Int](pkconvertedbezierpointreference/pointcount.md)
  The total number of B-Spline control points in the path.
- [var location: CGPoint](pkconvertedbezierpointreference/location.md)
  The location of the cubic uniform B-Spline control point.
- [var bezierSegmentIndex: Int](pkconvertedbezierpointreference/beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.
### Using Swift types
- [PKStrokePath.ConvertedBezierPoint](pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkconvertedbezierpointreference)*