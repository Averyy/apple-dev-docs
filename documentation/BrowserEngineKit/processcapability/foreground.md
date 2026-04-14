# ProcessCapability.foreground

**Framework**: BrowserEngineKit  
**Kind**: case

A process capability for work in the foreground.

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

#### Discussion

This capability grants the helper extension process the ability to run at foreground priority and work on behalf of the host process while the host process is in the foreground.

Use this capability while your browser app is in the foreground to allow extensions that support the browser’s UI to run at foreground priority.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  A process capability for work in the background.
- [ProcessCapability.suspended](processcapability/suspended.md)
  A process capability that grants residency in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents the provision of a capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/foreground)*