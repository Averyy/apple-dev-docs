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
  The operating system permits the helper extension process to run in the background to finish work.
- [ProcessCapability.foreground](processcapability/foreground.md)
  The operating system permits the helper extension process to run at foreground priority to work on behalf of the browser app.
- [ProcessCapability.suspended](processcapability/suspended.md)
  The operating system permits the helper extension process to remain resident in a suspended state.
- [ProcessCapability.Grant](processcapability/grant.md)
  An object that represents a granted capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/processcapability/mediaplaybackandcapture(environment:))*