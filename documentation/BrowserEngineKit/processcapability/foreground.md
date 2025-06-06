# ProcessCapability.foreground

**Framework**: BrowserEngineKit  
**Kind**: case

The operating system permits the helper extension process to run at foreground priority to work on behalf of the browser app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
case foreground
```

## Mentions

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)

#### Overview

Use this capability while your browser app is in the foreground, to allow extensions that support the browser’s UI to run at foreground priority.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  The operating system permits the helper extension process to run in the background to finish work.
- [ProcessCapability.suspended](processcapability/suspended.md)
  The operating system permits the helper extension process to remain resident in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents a granted capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/foreground)*