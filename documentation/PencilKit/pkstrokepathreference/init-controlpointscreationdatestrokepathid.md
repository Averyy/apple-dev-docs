# init(controlPoints:creationDate:strokePathID:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke path with the specified control points and a unique identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(controlPoints: [PKStrokePoint], creationDate: Date, strokePathID: UUID)
```

#### Discussion

> ⚠️ **Warning**: Using multiple stroke paths with identical IDs but different control points will result in undefined rendering behavior. Ensure each stroke path has a unique identifier.

## Parameters

- `controlPoints`: An array of control points for a cubic B-spline.
- `creationDate`: The start time of this path.
- `strokePathID`: The unique identity of the stroke path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/init(controlpoints:creationdate:strokepathid:))*