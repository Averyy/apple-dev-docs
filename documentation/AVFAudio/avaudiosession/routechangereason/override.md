# AVAudioSession.RouteChangeReason.override

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A value that indicates that the output route was overridden by the app.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case override
```

```c
AVAudioSessionRouteChangeReasonOverride
```

## See Also

### Identifying route change reasons
- [AVAudioSession.RouteChangeReason.unknown](./unknown.md)
  A value that indicates the reason for the change is unknown.
- [AVAudioSession.RouteChangeReason.newDeviceAvailable](./newdeviceavailable.md)
  A value that indicates a user action, such as plugging in a headset, has made a preferred audio route available.
- [AVAudioSession.RouteChangeReason.oldDeviceUnavailable](./olddeviceunavailable.md)
  A value that indicates that the previous audio output path is no longer available.
- [AVAudioSession.RouteChangeReason.categoryChange](./categorychange.md)
  A value that indicates that the category of the session object changed.
- [AVAudioSession.RouteChangeReason.wakeFromSleep](./wakefromsleep.md)
  A value that indicates that the route changed when the device woke up from sleep.
- [AVAudioSession.RouteChangeReason.noSuitableRouteForCategory](./nosuitablerouteforcategory.md)
  A value that indicates that the route changed because no suitable route is now available for the specified category.
- [AVAudioSession.RouteChangeReason.routeConfigurationChange](./routeconfigurationchange.md)
  A value that indicates that the configuration for a set of I/O ports has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routechangereason/override)*