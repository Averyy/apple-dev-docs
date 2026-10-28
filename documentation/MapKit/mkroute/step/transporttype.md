# transportType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The transport type of the step.

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
var transportType: MKDirectionsTransportType { get }
```

```objc
@property (nonatomic, readonly) MKDirectionsTransportType transportType;
```

## Discussion

This property reflects the transport type employed by the step and may differ from the transport type of the overall route.

## See Also

### Getting additional step details
- [var instructions: String](./instructions.md)
  The written instructions for following the path that the step represents.
- [var notice: String?](./notice.md)
  Additional notices that apply to the step.
- [var distance: CLLocationDistance](./distance.md)
  The step distance, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step/transporttype)*