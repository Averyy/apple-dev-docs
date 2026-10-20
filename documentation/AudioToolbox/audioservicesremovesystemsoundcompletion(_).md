# AudioServicesRemoveSystemSoundCompletion(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Unregisters any completion callback functions that were registered for a specified system sound.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioServicesRemoveSystemSoundCompletion(_ inSystemSoundID: SystemSoundID)
```

```c
extern void AudioServicesRemoveSystemSoundCompletion(SystemSoundID inSystemSoundID);
```

## Parameters

- `inSystemSoundID`: The system sound for which callback functions should be removed.

## See Also

### Adding and Removing System Sound Callbacks
- [func AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop?, CFString?, AudioServicesSystemSoundCompletionProc, UnsafeMutableRawPointer?) -> OSStatus](./audioservicesaddsystemsoundcompletion%28_,_,_,_,_%29.md)
  Registers a callback function that is invoked when a specified system sound finishes playing.
- [typealias AudioServicesSystemSoundCompletionProc](./audioservicessystemsoundcompletionproc.md)
  A function the system invokes when a system sound finishes playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesremovesystemsoundcompletion(_:))*