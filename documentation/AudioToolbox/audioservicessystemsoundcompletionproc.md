# AudioServicesSystemSoundCompletionProc

**Framework**: Audio Toolbox  
**Kind**: typealias

A function the system invokes when a system sound finishes playing.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioServicesSystemSoundCompletionProc = (SystemSoundID, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Because a system sound may play for up to 30 seconds, the [`AudioServicesPlaySystemSound(_:)`](audioservicesplaysystemsound(_:).md) function executes asynchronously (that is, it returns immediately), and calls this function when the sound finishes playing. You can use this callback, for example, to help you avoid playing a second sound while a first sound is still playing.

## Parameters

- `ssID`: The system sound that has finished playing.
- `clientData`: App data that you specified when registering the callback function.

## See Also

- [func AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop?, CFString?, AudioServicesSystemSoundCompletionProc, UnsafeMutableRawPointer?) -> OSStatus](audioservicesaddsystemsoundcompletion(_:_:_:_:_:).md)
  Registers a callback function that is invoked when a specified system sound finishes playing.
- [func AudioServicesRemoveSystemSoundCompletion(SystemSoundID)](audioservicesremovesystemsoundcompletion(_:).md)
  Unregisters any completion callback functions that were registered for a specified system sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicessystemsoundcompletionproc)*