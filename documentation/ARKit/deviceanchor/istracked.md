# isTracked

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether ARKit is tracking the device.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var isTracked: Bool { get }
```

## See Also

### Inspecting a device anchor
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The transform from the device to the origin coordinate system.
- [var trackingState: DeviceAnchor.TrackingState](./trackingstate-swift.property.md)
  Tracking state of this anchor
- [DeviceAnchor.TrackingState](./trackingstate-swift.enum.md)
  Values that describe the tracking state of a device anchor.
- [var description: String](./description.md)
  A textual representation of this anchor.
- [var id: UUID](./id.md)
  The unique identifier of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/deviceanchor/istracked)*