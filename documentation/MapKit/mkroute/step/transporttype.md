# transportType

**Framework**: MapKit  
**Kind**: property

The transport type of the step.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var transportType: MKDirectionsTransportType { get }
```

#### Discussion

This property reflects the transport type employed by the step and may differ from the transport type of the overall route.

## See Also

- [var instructions: String](mkroute/step/instructions.md)
  The written instructions for following the path that the step represents.
- [var notice: String?](mkroute/step/notice.md)
  Additional notices that apply to the step.
- [var distance: CLLocationDistance](mkroute/step/distance.md)
  The step distance, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step/transporttype)*