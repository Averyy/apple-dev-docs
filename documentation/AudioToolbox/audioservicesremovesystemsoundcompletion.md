# AudioServicesRemoveSystemSoundCompletion(_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

## Parameters

- `inSystemSoundID`: The system sound for which callback functions should be removed.

## See Also

- [func AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop?, CFString?, AudioServicesSystemSoundCompletionProc, UnsafeMutableRawPointer?) -> OSStatus](audioservicesaddsystemsoundcompletion(_:_:_:_:_:).md)
  Registers a callback function that is invoked when a specified system sound finishes playing.
- [typealias AudioServicesSystemSoundCompletionProc](audioservicessystemsoundcompletionproc.md)
  A function the system invokes when a system sound finishes playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicesremovesystemsoundcompletion(_:))*