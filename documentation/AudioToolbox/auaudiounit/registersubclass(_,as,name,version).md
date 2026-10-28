# registerSubclass(_:as:name:version:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Type Method

Registers an audio unit subclass.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func registerSubclass(_ cls: AnyClass, as componentDescription: AudioComponentDescription, name: String, version: UInt32)
```

```objc
+ (void) registerSubclass:(Class) cls asComponentDescription:(AudioComponentDescription) componentDescription name:(NSString *) name version:(UInt32) version;
```

## Discussion

This method dynamically registers the supplied [`AUAudioUnit`](../auaudiounit.md) subclass with the Audio Component system, in the context of the current process only. After you’ve registered the subclass, instantiate it by calling one of the following:

- The [`init(componentDescription:)`](./init%28componentdescription%29.md) method.
- The [`init(componentDescription:options:)`](./init%28componentdescription,options%29.md) method.
- The [`AVAudioUnit`](../../AVFAudio/avaudiounit.md) [`instantiate(with:options:completionHandler:)`](../../AVFAudio/avaudiounit/instantiate%28with,options,completionhandler%29.md) method.
- The [`AudioComponentInstanceNew(_:_:)`](../audiocomponentinstancenew%28_,_%29.md) function.

## Parameters

- `cls`: An [`AUAudioUnit`](../auaudiounit.md) subclass.
- `componentDescription`: The component to register.
- `name`: The component’s name, using the convention `<manufacturer name>:<audio unit name>`.
- `version`: The component’s version.

## See Also

### Customizing the Audio Unit Behavior
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](./shouldchange%28to,for%29.md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](./setrenderresourcesallocated%28_%29.md)
  Sets the Boolean value of the [`renderResourcesAllocated`](./renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](./internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](./midioutputbuffersizehint.md)
- [typealias AUInternalRenderBlock](../auinternalrenderblock.md)
  A block to render the audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/registersubclass(_:as:name:version:))*