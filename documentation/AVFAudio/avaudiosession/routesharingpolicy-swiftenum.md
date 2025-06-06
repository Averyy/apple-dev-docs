# AVAudioSession.RouteSharingPolicy

**Framework**: AVFAudio  
**Kind**: enum

Cases that indicate the possible route-sharing policies for an audio session.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum RouteSharingPolicy
```

#### Overview

A route-sharing policy allows you to specify that an audio session should route its output to somewhere other than the default system output when alternative routes are available.

## Topics

### Route-sharing policies
- [AVAudioSession.RouteSharingPolicy.default](avaudiosession/routesharingpolicy-swift.enum/default.md)
  A policy that follows standard rules for routing audio output.
- [AVAudioSession.RouteSharingPolicy.longFormAudio](avaudiosession/routesharingpolicy-swift.enum/longformaudio.md)
  A policy that routes output to the shared long-form audio output.
- [AVAudioSession.RouteSharingPolicy.longFormVideo](avaudiosession/routesharingpolicy-swift.enum/longformvideo.md)
  A policy that routes output to the shared long-form video output.
- [AVAudioSession.RouteSharingPolicy.independent](avaudiosession/routesharingpolicy-swift.enum/independent.md)
  A policy in which the route picker UI directs videos to a wireless route.
- [static var longForm: AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.enum/longform.md)
  A policy that routes output to the shared long-form audio output.
### Initializers
- [init?(rawValue: UInt)](avaudiosession/routesharingpolicy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var routeSharingPolicy: AVAudioSession.RouteSharingPolicy](avaudiosession/routesharingpolicy-swift.property.md)
  The active route-sharing policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.enum)*