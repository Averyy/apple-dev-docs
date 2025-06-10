# AVAudioSession.RouteChangeReason

**Framework**: AVFAudio  
**Kind**: enum

Constants that indicate the reason for an audio route change.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum RouteChangeReason
```

## Mentions

- [Responding to audio route changes](responding-to-audio-route-changes.md)

#### Overview

These constants appear as possible values for the [`AVAudioSessionRouteChangeReasonKey`](avaudiosessionroutechangereasonkey.md) key in the `userInfo` dictionary in a [`routeChangeNotification`](avaudiosession/routechangenotification.md) notification.

## Topics

### Route Change Reasons
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
- [AVAudioSession.RouteChangeReason.wakeFromSleep](avaudiosession/routechangereason/wakefromsleep.md)
  A value that indicates that the route changed when the device woke up from sleep.
- [AVAudioSession.RouteChangeReason.noSuitableRouteForCategory](avaudiosession/routechangereason/nosuitablerouteforcategory.md)
  A value that indicates that the route changed because no suitable route is now available for the specified category.
- [AVAudioSession.RouteChangeReason.routeConfigurationChange](avaudiosession/routechangereason/routeconfigurationchange.md)
  A value that indicates that the configuration for a set of I/O ports has changed.
### Initializers
- [init?(rawValue: UInt)](avaudiosession/routechangereason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routechangereason)*