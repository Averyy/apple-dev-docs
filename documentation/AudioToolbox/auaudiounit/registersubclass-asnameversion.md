# registerSubclass(_:as:name:version:)

**Framework**: Audio Toolbox  
**Kind**: method

Registers an audio unit subclass.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func registerSubclass(_ cls: AnyClass, as componentDescription: AudioComponentDescription, name: String, version: UInt32)
```

#### Discussion

This method dynamically registers the supplied [`AUAudioUnit`](auaudiounit.md) subclass with the Audio Component system, in the context of the current process only. After you’ve registered the subclass, instantiate it by calling one of the following:

- The [`init(componentDescription:)`](auaudiounit/init(componentdescription:).md) method.
- The [`init(componentDescription:options:)`](auaudiounit/init(componentdescription:options:).md) method.
- The [`AVAudioUnit`](https://developer.apple.com/documentation/AVFAudio/AVAudioUnit) [`instantiate(with:options:completionHandler:)`](https://developer.apple.com/documentation/AVFAudio/AVAudioUnit/instantiate(with:options:completionHandler:)) method.
- The [`AudioComponentInstanceNew(_:_:)`](audiocomponentinstancenew(_:_:).md) function.

## Parameters

- `cls`: An   subclass.
- `componentDescription`: The component to register.
- `name`: The component’s name, using the convention  .
- `version`: The component’s version.

## See Also

- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](auaudiounit/shouldchange(to:for:).md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](auaudiounit/setrenderresourcesallocated(_:).md)
  Sets the Boolean value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](auaudiounit/internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](auaudiounit/midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/registersubclass(_:as:name:version:))*