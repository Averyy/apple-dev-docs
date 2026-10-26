# playbackControl

**Framework**: AVSystemRouting  
**Kind**: property  
**Role**: Instance Property

The playback control interface for the remote session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (readonly, nullable) NSObject<AVPlaybackUserInterfaceControllable> * playbackControl;
```

#### Discussion

This property is always non-nil when obtained from a successful call to [`start()`](../avsystemroutesession-gp78/start%28%29.md).

> ❗ **Important**: Always update media playback state information regularly in the playbackControl object to ensure the system displays accurate information about the current media play state across a person’s devices and in system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-4mo0j/playbackcontrol)*