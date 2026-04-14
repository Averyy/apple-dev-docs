# ProcessCapability.background

**Framework**: BrowserEngineKit  
**Kind**: case

A process capability for work in the background.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
case background
```

#### Discussion

This capability grants the helper extension process the ability to run in the background to finish work.

## See Also

- [ProcessCapability.foreground](processcapability/foreground.md)
  A process capability for work in the foreground.
- [ProcessCapability.suspended](processcapability/suspended.md)
  A process capability that grants residency in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents the provision of a capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/background)*