# instructions

**Framework**: MapKit  
**Kind**: property

The written instructions for following the path that the step represents.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var instructions: String { get }
```

#### Discussion

The framework localizes the string in this property according to the user’s language preferences. You can present this string to the user from your app’s interface.

## See Also

- [var notice: String?](mkroute/step/notice.md)
  Additional notices that apply to the step.
- [var distance: CLLocationDistance](mkroute/step/distance.md)
  The step distance, in meters.
- [var transportType: MKDirectionsTransportType](mkroute/step/transporttype.md)
  The transport type of the step.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/step/instructions)*