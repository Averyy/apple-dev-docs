# ProcessCapability.Grant

**Framework**: BrowserEngineKit  
**Kind**: struct

An object that represents a granted capability.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
struct Grant
```

## Mentions

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)

## Topics

### Testing and changing validity
- [var isValid: Bool](processcapability/grant/isvalid.md)
  A Boolean that indicates whether the operating system has granted the capability to the browser extension process.
- [func invalidate()](processcapability/grant/invalidate.md)
  Invalidates the grant, removing the capability from the process it was granted to.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  The operating system permits the helper extension process to run in the background to finish work.
- [ProcessCapability.foreground](processcapability/foreground.md)
  The operating system permits the helper extension process to run at foreground priority to work on behalf of the browser app.
- [ProcessCapability.suspended](processcapability/suspended.md)
  The operating system permits the helper extension process to remain resident in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/grant)*