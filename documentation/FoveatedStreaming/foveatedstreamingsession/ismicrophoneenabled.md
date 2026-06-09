# isMicrophoneEnabled

**Framework**: Foveated Streaming  
**Kind**: property

Whether the microphone is currently enabled for this session.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
final var isMicrophoneEnabled: Bool { get set }
```

#### Discussion

Set this to `true` to unmute or `false` to mute while the session is `.connected`. If the daemon rejects the call (e.g. session not connected or missing TCC authorization), the value remains unchanged and an error is logged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/ismicrophoneenabled)*