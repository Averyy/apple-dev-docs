# AVAudioSession.RouteChangeReason

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the reason for an audio route change.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum RouteChangeReason
```

```c
enum AVAudioSessionRouteChangeReason : NSUInteger;
```

## Mentions

- [Responding to audio route changes](../responding-to-audio-route-changes.md)

#### Overview

These constants appear as possible values for the [`AVAudioSessionRouteChangeReasonKey`](../avaudiosessionroutechangereasonkey.md) key in the `userInfo` dictionary in a [`routeChangeNotification`](./routechangenotification.md) notification.

## Topics

### Creating a route change reason
- [init?(rawValue: UInt)](./routechangereason/init%28rawvalue%29.md)
### Identifying route change reasons
- [AVAudioSession.RouteChangeReason.unknown](./routechangereason/unknown.md)
  A value that indicates the reason for the change is unknown.
- [AVAudioSession.RouteChangeReason.newDeviceAvailable](./routechangereason/newdeviceavailable.md)
  A value that indicates a user action, such as plugging in a headset, has made a preferred audio route available.
- [AVAudioSession.RouteChangeReason.oldDeviceUnavailable](./routechangereason/olddeviceunavailable.md)
  A value that indicates that the previous audio output path is no longer available.
- [AVAudioSession.RouteChangeReason.categoryChange](./routechangereason/categorychange.md)
  A value that indicates that the category of the session object changed.
- [AVAudioSession.RouteChangeReason.override](./routechangereason/override.md)
  A value that indicates that the output route was overridden by the app.
- [AVAudioSession.RouteChangeReason.wakeFromSleep](./routechangereason/wakefromsleep.md)
  A value that indicates that the route changed when the device woke up from sleep.
- [AVAudioSession.RouteChangeReason.noSuitableRouteForCategory](./routechangereason/nosuitablerouteforcategory.md)
  A value that indicates that the route changed because no suitable route is now available for the specified category.
- [AVAudioSession.RouteChangeReason.routeConfigurationChange](./routechangereason/routeconfigurationchange.md)
  A value that indicates that the configuration for a set of I/O ports has changed.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routechangereason)*