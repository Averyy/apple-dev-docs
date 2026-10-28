# PKStrokePath.ConvertedBezierPoint

**Framework**: PencilKit  
**Kind**: struct  
**Role**: Structure

Information about a B-spline control point converted from a Bézier path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ConvertedBezierPoint
```

## Mentions

- [Importing Bézier path data into PencilKit](../importing-external-drawing-data-into-pencilkit.md)

## Overview

`ConvertedBezierPoint` values are passed one at a time to the `pointProvider` closure of [`init(bezierPath:creationDate:pointProvider:)`](./init%28bezierpath,creationdate,pointprovider%29.md). Use the provided location, index, and segment information to initialize each `PKStrokePoint` with appropriate size, opacity, force, and other drawing properties.

## Topics

### Getting the point data
- [let index: Int](./convertedbezierpoint/index.md)
  The index of the point along the path.
- [let pointCount: Int](./convertedbezierpoint/pointcount.md)
  The total number of B-Spline control points in the path.
- [let location: CGPoint](./convertedbezierpoint/location.md)
  The location of the cubic uniform B-Spline control point.
- [let bezierSegmentIndex: Int](./convertedbezierpoint/beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.
### Using reference types
- [class PKConvertedBezierPointReference](../pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.

## See Also

### Creating a new stroke path
- [init()](./init%28%29.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date)](./init%28controlpoints,creationdate%29.md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](./init%28controlpoints,creationdate,id%29.md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](./init%28bezierpath,creationdate,pointprovider%29.md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/convertedbezierpoint)*