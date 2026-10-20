# routeSharingPolicy

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The active route-sharing policy.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var routeSharingPolicy: AVAudioSession.RouteSharingPolicy { get }
```

```objc
@property (readonly) AVAudioSessionRouteSharingPolicy routeSharingPolicy;
```

#### Discussion

Use this value to indicate that the system should route this app’s audio somewhere other than the default system output when other suitable alternative routes exist.

## See Also

### Inspecting the route sharing policy
- [AVAudioSession.RouteSharingPolicy](./routesharingpolicy-swift.enum.md)
  Cases that indicate the possible route-sharing policies for an audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/routesharingpolicy-swift.property)*