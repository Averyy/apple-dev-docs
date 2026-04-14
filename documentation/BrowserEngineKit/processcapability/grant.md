# ProcessCapability.Grant

**Framework**: BrowserEngineKit  
**Kind**: struct

An object that represents the provision of a capability.

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
  A Boolean value that indicates whether the system honors a granted capability for the browser extension process.
- [func invalidate()](processcapability/grant/invalidate.md)
  Invalidates the grant, removing the capability from the process it was granted to.

## See Also

- [ProcessCapability.background](processcapability/background.md)
  A process capability for work in the background.
- [ProcessCapability.foreground](processcapability/foreground.md)
  A process capability for work in the foreground.
- [ProcessCapability.suspended](processcapability/suspended.md)
  A process capability that grants residency in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/grant)*