# AVAudioSession.RouteSelection

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

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

### Creating a route selection
- [init?(rawValue: Int)](./routeselection/init%28rawvalue%29.md)
### Identifying the selected route
- [AVAudioSession.RouteSelection.none](./routeselection/none.md)
  No route is selected.
- [AVAudioSession.RouteSelection.local](./routeselection/local.md)
  The local device is selected.
- [AVAudioSession.RouteSelection.external](./routeselection/external.md)
  An external device is selected.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Preparing for long-form video playback
- [func prepareRouteSelectionForPlayback(completionHandler: (Bool, AVAudioSession.RouteSelection) -> Void)](./preparerouteselectionforplayback%28completionhandler%29.md)
  Prepares the route selection for long-form video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routeselection)*