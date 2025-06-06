# init(controlPoints:creationDate:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke path with the cubic B-spline control points and a date that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(controlPoints: [PKStrokePoint], creationDate: Date)
```

## Parameters

- `controlPoints`: An array of control points for a cubic B-spline.
- `creationDate`: The creation time of this path. The   of points in this stroke path is relative to this date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/init(controlpoints:creationdate:))*