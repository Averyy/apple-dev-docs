# AVAudioSession.RouteChangeReason.wakeFromSleep

**Framework**: AVFAudio  
**Kind**: case

A value that indicates that the route changed when the device woke up from sleep.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case wakeFromSleep
```

## See Also

- [AVAudioSession.RouteChangeReason.unknown](avaudiosession/routechangereason/unknown.md)
  A value that indicates the reason for the change is unknown.
- [AVAudioSession.RouteChangeReason.newDeviceAvailable](avaudiosession/routechangereason/newdeviceavailable.md)
  A value that indicates a user action, such as plugging in a headset, has made a preferred audio route available.
- [AVAudioSession.RouteChangeReason.oldDeviceUnavailable](avaudiosession/routechangereason/olddeviceunavailable.md)
  A value that indicates that the previous audio output path is no longer available.
- [AVAudioSession.RouteChangeReason.categoryChange](avaudiosession/routechangereason/categorychange.md)
  A value that indicates that the category of the session object changed.
- [AVAudioSession.RouteChangeReason.override](avaudiosession/routechangereason/override.md)
  A value that indicates that the output route was overridden by the app.
- [AVAudioSession.RouteChangeReason.noSuitableRouteForCategory](avaudiosession/routechangereason/nosuitablerouteforcategory.md)
  A value that indicates that the route changed because no suitable route is now available for the specified category.
- [AVAudioSession.RouteChangeReason.routeConfigurationChange](avaudiosession/routechangereason/routeconfigurationchange.md)
  A value that indicates that the configuration for a set of I/O ports has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routechangereason/wakefromsleep)*