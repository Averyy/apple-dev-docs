# ProcessCapability

**Framework**: BrowserEngineKit  
**Kind**: enum  
**Role**: Enumeration

Capabilities of a helper extension process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
enum ProcessCapability
```

## Mentions

- [Managing the browser extension life cycle](./managing-the-browser-extension-lifecycle.md)

## Overview

To grant a capability to an extension, call the `grantCapability(_:)` method for the relevant process:

- **Web content extension**: [`grantCapability(_:)`](./webcontentprocess/grantcapability%28_%29.md)
- **Networking extension**: [`grantCapability(_:)`](./networkingprocess/grantcapability%28_%29.md)
- **Rendering extension**: [`grantCapability(_:)`](./renderingprocess/grantcapability%28_%29.md)

These methods return a [`ProcessCapability.Grant`](./processcapability/grant.md) object.

When your extension no longer needs the capability, call [`invalidate()`](./processcapability/grant/invalidate%28%29.md).

## Topics

### Granting capabilities
- [ProcessCapability.background](./processcapability/background.md)
  A process capability for work in the background.
- [ProcessCapability.foreground](./processcapability/foreground.md)
  A process capability for work in the foreground.
- [ProcessCapability.suspended](./processcapability/suspended.md)
  A process capability that grants residency in a suspended state.
- [case mediaPlaybackAndCapture(environment: MediaEnvironment)](./processcapability/mediaplaybackandcapture%28environment%29.md)
  The helper extension process may access media hardware required for media capture and playback.
- [ProcessCapability.Grant](./processcapability/grant.md)
  An object that represents the provision of a capability.
### Enumeration Cases
- [case screenCapture(environment: MediaEnvironment)](./processcapability/screencapture%28environment%29.md)
  The helper extension process may access AV hardware required for media capture and playback.
### Instance Methods
- [func activate() throws](./processcapability/activate%28%29.md)
  Activates the capability.
- [func request() throws -> ProcessCapability.Grant](./processcapability/request%28%29.md)
  Requests the capability to be granted to the current process.
- [func suspend() throws](./processcapability/suspend%28%29.md)
  Suspends the capability.

## See Also

### Extension capabilities
- [class BEProcessCapability](./beprocesscapability-76ijx.md)
  Capabilities of a helper extension process.
- [struct MediaEnvironment](./mediaenvironment.md)
  An object that identifies a media playback or streaming environment.
- [class BEMediaEnvironment](./bemediaenvironment-15xci.md)
  An object that identifies a media playback or streaming environment.
- [class BEWebContentFilter](./bewebcontentfilter.md)
  An object that represents a web content filter.
- [enum RenderingExtensionFeature](./renderingextensionfeature.md)
  Features of a rendering extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability)*