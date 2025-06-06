# distance

**Framework**: MapKit  
**Kind**: property

The step distance, in meters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var distance: CLLocationDistance { get }
```

#### Discussion

This property reflects the distance that the user covers while traversing the path of the step. It isn’t a lilnear distance between the start and end points of the step.

## See Also

- [var instructions: String](mkroute/step/instructions.md)
  The written instructions for following the path that the step represents.
- [var notice: String?](mkroute/step/notice.md)
  Additional notices that apply to the step.
- [var transportType: MKDirectionsTransportType](mkroute/step/transporttype.md)
  The transport type of the step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step/distance)*