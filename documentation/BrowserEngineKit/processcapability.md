# ProcessCapability

**Framework**: BrowserEngineKit  
**Kind**: enum

An enumeration that identifies capabilities that a browser app can grant to its extension processes.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
enum ProcessCapability
```

## Mentions

- [Managing the browser extension life cycle](managing-the-browser-extension-lifecycle.md)

#### Overview

To grant a capability to an extension, call the `grantCapability(_:)` method for the relevant process:

These methods return a [`ProcessCapability.Grant`](processcapability/grant.md) object. When your extension no longer needs the capability, call [`invalidate()`](processcapability/grant/invalidate().md).

## Topics

### Granting capabilities to browser extension processes
- [ProcessCapability.background](processcapability/background.md)
  The operating system permits the helper extension process to run in the background to finish work.
- [ProcessCapability.foreground](processcapability/foreground.md)
  The operating system permits the helper extension process to run at foreground priority to work on behalf of the browser app.
- [ProcessCapability.suspended](processcapability/suspended.md)
  The operating system permits the helper extension process to remain resident in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](processcapability/mediaplaybackandcapture(environment:).md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents a granted capability.

## See Also

- [struct MediaEnvironment](mediaenvironment.md)
  An object that identifies a media playback or streaming environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability)*