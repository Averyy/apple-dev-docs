# suspended

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

A capability that enables an extension process to stay in a suspended state.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
+ (instancetype) suspended;
```

#### Discussion

This capability grants the helper extension process the ability to stay in a suspended state, although the system doesn’t allocate it any CPU time.

## See Also

### Granting capabilities to browser extension processes
- [+ background](./background.md)
  A capability that enables an extension process to work in the background.
- [+ foreground](./foreground.md)
  A capability that enables an extension process to do foreground priority work.
- [+ mediaPlaybackAndCaptureWithEnvironment:](./mediaplaybackandcapturewithenvironment_.md)
  A capability that enables an extension process to access hardware that media capture and playback require.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beprocesscapability-7av05/suspended)*