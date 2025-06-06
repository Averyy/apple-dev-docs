# AVAudioSession.RouteSelection

**Framework**: AVFAudio  
**Kind**: enum

Constants used to define the active route selection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum RouteSelection
```

## Topics

### Constants
- [AVAudioSession.RouteSelection.none](avaudiosession/routeselection/none.md)
  No route is selected.
- [AVAudioSession.RouteSelection.local](avaudiosession/routeselection/local.md)
  The local device is selected.
- [AVAudioSession.RouteSelection.external](avaudiosession/routeselection/external.md)
  An external device is selected.
### Initializers
- [init?(rawValue: Int)](avaudiosession/routeselection/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func prepareRouteSelectionForPlayback(completionHandler: (Bool, AVAudioSession.RouteSelection) -> Void)](avaudiosession/preparerouteselectionforplayback(completionhandler:).md)
  Prepares the route selection for long-form video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routeselection)*