# AURenderCallback

**Framework**: Audio Toolbox  
**Kind**: typealias

Called by the system when an audio unit requires input samples, or before and after a render operation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AURenderCallback = (UnsafeMutableRawPointer, UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>?) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

If you named your callback function `MyAURenderCallback`, you would declare it like this:

##### Discussion

You can use this callback function with both the audio unit render notification API (see the [`AudioUnitAddRenderNotify(_:_:_:)`](audiounitaddrendernotify(_:_:_:).md) function) and the render input callback (see the `kAudioUnitProperty_SetRenderCallback` property).

As a notification listener, the system invokes this callback before and after an audio unit’s render operations.

As a render operation input callback, it is invoked when an audio unit requires input samples for the input bus that the callback is attached to.

## Parameters

- `inRefCon`: Custom data that you provided when registering your callback with the audio unit.
- `ioActionFlags`: Flags used to describe more about the context of this call (pre or post in the notify case for instance).
- `inTimeStamp`: The timestamp associated with this call of audio unit render.
- `inBusNumber`: The bus number associated with this call of audio unit render.
- `inNumberFrames`: The number of sample frames that will be represented in the audio data in the provided ioData parameter.
- `ioData`: The AudioBufferList that will be used to contain the rendered or provided audio data.

## See Also

- [func AudioUnitRender(AudioUnit, UnsafeMutablePointer<AudioUnitRenderActionFlags>?, UnsafePointer<AudioTimeStamp>, UInt32, UInt32, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audiounitrender(_:_:_:_:_:_:).md)
  Initiates a rendering cycle for an audio unit.
- [func AudioUnitAddRenderNotify(AudioUnit, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](audiounitaddrendernotify(_:_:_:).md)
  Registers a callback to receive audio unit render notifications.
- [func AudioUnitRemoveRenderNotify(AudioUnit, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](audiounitremoverendernotify(_:_:_:).md)
  Unregisters a previously-registered render listener callback function.
- [struct AudioUnitRenderActionFlags](audiounitrenderactionflags.md)
  Flags for configuring audio unit rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aurendercallback)*