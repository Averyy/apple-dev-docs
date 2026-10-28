# AVAudioSession.RouteSharingPolicy

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Cases that indicate the possible route-sharing policies for an audio session.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum RouteSharingPolicy
```

```c
enum AVAudioSessionRouteSharingPolicy : NSUInteger;
```

## Overview

A route-sharing policy allows you to specify that an audio session should route its output to somewhere other than the default system output when alternative routes are available.

## Topics

### Creating a route-sharing policy
- [init?(rawValue: UInt)](./routesharingpolicy-swift.enum/init%28rawvalue%29.md)
### Choosing a route-sharing policy
- [AVAudioSession.RouteSharingPolicy.default](./routesharingpolicy-swift.enum/default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](./routesharingpolicy-swift.enum/longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](./routesharingpolicy-swift.enum/longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [AVAudioSession.RouteSharingPolicy.independent](./routesharingpolicy-swift.enum/independent.md)
  A policy in which the route picker UI directs videos to a wireless route.
- [static var longForm: AVAudioSession.RouteSharingPolicy](./routesharingpolicy-swift.enum/longform.md)
  A policy that routes output to the shared long-form audio output.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting the route sharing policy
- [var routeSharingPolicy: AVAudioSession.RouteSharingPolicy](./routesharingpolicy-swift.property.md)
  The active route-sharing policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum)*