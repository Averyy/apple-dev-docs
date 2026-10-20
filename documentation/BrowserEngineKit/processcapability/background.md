# ProcessCapability.background

**Framework**: BrowserEngineKit  
**Kind**: case  
**Role**: Case

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

### Granting capabilities
- [ProcessCapability.foreground](./foreground.md)
  A process capability for work in the foreground.
- [ProcessCapability.suspended](./suspended.md)
  A process capability that grants residency in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](./mediaplaybackandcapture%28environment%29.md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](./grant.md)
  An object that represents the provision of a capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/background)*