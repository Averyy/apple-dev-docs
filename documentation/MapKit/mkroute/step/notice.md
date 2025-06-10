# notice

**Framework**: MapKit  
**Kind**: property

Additional notices that apply to the step.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var notice: String? { get }
```

#### Discussion

Notices may include legal information or warning notices that apply to the step. For example, if the step crosses railroad tracks, it might contain a notice that warns the user not to cross the tracks when the lights are flashing.

## See Also

- [var instructions: String](mkroute/step/instructions.md)
  The written instructions for following the path that the step represents.
- [var distance: CLLocationDistance](mkroute/step/distance.md)
  The step distance, in meters.
- [var transportType: MKDirectionsTransportType](mkroute/step/transporttype.md)
  The transport type of the step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step/notice)*