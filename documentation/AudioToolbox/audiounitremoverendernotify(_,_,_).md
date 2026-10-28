# AudioUnitRemoveRenderNotify(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Unregisters a previously-registered render listener callback function.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioUnitRemoveRenderNotify(_ inUnit: AudioUnit, _ inProc: AURenderCallback, _ inProcUserData: UnsafeMutableRawPointer?) -> OSStatus
```

```c
extern OSStatus AudioUnitRemoveRenderNotify(AudioUnit inUnit, AURenderCallback inProc, void *inProcUserData);
```

## Return Value

A result code.

## Parameters

- `inUnit`: The audio unit that you no longer want to receive render notifications from.
- `inProc`: The callback function that you previously registered and are now unregistering.
- `inProcUserData`: The custom data that you provided when registering the callback function.

## See Also

### Rendering the Audio
- [func AudioUnitRender(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](./audiounitrender%28_,_,_,_,_,_%29.md)
  Initiates a rendering cycle for an audio unit.
- [func AudioUnitAddRenderNotify(AudioUnit, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](./audiounitaddrendernotify%28_,_,_%29.md)
  Registers a callback to receive audio unit render notifications.
- [typealias AURenderCallback](./aurendercallback.md)
  Called by the system when an audio unit requires input samples, or before and after a render operation.
- [struct AudioUnitRenderActionFlags](./audiounitrenderactionflags.md)
  Flags for configuring audio unit rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitremoverendernotify(_:_:_:))*