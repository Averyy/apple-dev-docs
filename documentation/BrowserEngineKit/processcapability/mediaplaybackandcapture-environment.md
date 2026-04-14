# ProcessCapability.mediaPlaybackAndCapture(environment:)

**Framework**: BrowserEngineKit  
**Kind**: case

The helper extension process may access media hardware required for media capture and playback.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
case mediaPlaybackAndCapture(environment: MediaEnvironment)
```

#### Discussion

> ❗ **Important**:  You need to call [`activate()`](mediaenvironment/activate().md) on the media environment before you grant this capability to an extension.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  A process capability for work in the background.
- [ProcessCapability.foreground](processcapability/foreground.md)
  A process capability for work in the foreground.
- [ProcessCapability.suspended](processcapability/suspended.md)
  A process capability that grants residency in a suspended state.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents the provision of a capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/mediaplaybackandcapture(environment:))*