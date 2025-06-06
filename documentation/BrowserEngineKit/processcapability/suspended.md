# ProcessCapability.suspended

**Framework**: BrowserEngineKit  
**Kind**: case

The operating system permits the helper extension process to remain resident in a suspended state.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
case suspended
```

#### Overview

While a helper extension process has this capability, the operating system doesn’t grant it CPU time.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  The operating system permits the helper extension process to run in the background to finish work.
- [ProcessCapability.foreground](processcapability/foreground.md)
  The operating system permits the helper extension process to run at foreground priority to work on behalf of the browser app.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents a granted capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/suspended)*