# ProcessCapability.suspended

**Framework**: BrowserEngineKit  
**Kind**: case

A process capability that grants residency in a suspended state.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
case suspended
```

#### Discussion

This capability grants the helper extension process the ability to stay in a suspended state, although the system won’t allocate it any CPU time.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  A process capability for work in the background.
- [ProcessCapability.foreground](processcapability/foreground.md)
  A process capability for work in the foreground.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents the provision of a capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/suspended)*