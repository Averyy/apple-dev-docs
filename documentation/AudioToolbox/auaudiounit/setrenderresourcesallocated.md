# setRenderResourcesAllocated(_:)

**Framework**: Audio Toolbox  
**Kind**: method

Sets the Boolean value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func setRenderResourcesAllocated(_ flag: Bool)
```

#### Discussion

In the base class implementation of the [`allocateRenderResources()`](auaudiounit/allocaterenderresources().md) method, the value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true). If the [`allocateRenderResources()`](auaudiounit/allocaterenderresources().md) method fails in a subclass, you must use this method to set the value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `flag`: A Boolean value that determines whether the audio unit has allocated its required rendering resources..

## See Also

- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](auaudiounit/registersubclass(_:as:name:version:).md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](auaudiounit/shouldchange(to:for:).md)
  This is called when you set the format on a bus.
- [var internalRenderBlock: AUInternalRenderBlock](auaudiounit/internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](auaudiounit/midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/setrenderresourcesallocated(_:))*