# AudioServicesSystemSoundCompletionProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A function the system invokes when a system sound finishes playing.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioServicesSystemSoundCompletionProc = (SystemSoundID, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(unsigned int, void *) AudioServicesSystemSoundCompletionProc;
```

## Discussion

Because a system sound may play for up to 30 seconds, the [`AudioServicesPlaySystemSound(_:)`](./audioservicesplaysystemsound%28_%29.md) function executes asynchronously (that is, it returns immediately), and calls this function when the sound finishes playing. You can use this callback, for example, to help you avoid playing a second sound while a first sound is still playing.

## Parameters

- `ssID`: The system sound that has finished playing.
- `clientData`: App data that you specified when registering the callback function.

## See Also

### Adding and Removing System Sound Callbacks
- [func AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop?, CFString?, AudioServicesSystemSoundCompletionProc, UnsafeMutableRawPointer?) -> OSStatus](./audioservicesaddsystemsoundcompletion%28_,_,_,_,_%29.md)
  Registers a callback function that is invoked when a specified system sound finishes playing.
- [func AudioServicesRemoveSystemSoundCompletion(SystemSoundID)](./audioservicesremovesystemsoundcompletion%28_%29.md)
  Unregisters any completion callback functions that were registered for a specified system sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioservicessystemsoundcompletionproc)*