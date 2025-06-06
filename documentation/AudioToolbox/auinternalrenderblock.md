# AUInternalRenderBlock

**Framework**: Audio Toolbox  
**Kind**: typealias

A block to render the audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUInternalRenderBlock = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AURenderEvent>?, AURenderPullInputBlock?) -> AUAudioUnitStatus
```

#### Discussion

This block is implemented in subclasses and should not be used by hosts.

The block returns an audio unit status result code. If instead an error is returned, the output data should be assumed to be invalid.

The block takes the following parameters:

## See Also

- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](auaudiounit/registersubclass(_:as:name:version:).md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](auaudiounit/shouldchange(to:for:).md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](auaudiounit/setrenderresourcesallocated(_:).md)
  Sets the Boolean value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](auaudiounit/internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](auaudiounit/midioutputbuffersizehint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)*