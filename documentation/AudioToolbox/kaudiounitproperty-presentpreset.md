# kAudioUnitProperty_PresentPreset

**Framework**: Audio Toolbox  
**Kind**: var

The active factory preset for an audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitProperty_PresentPreset: AudioUnitPropertyID { get }
```

#### Discussion

A read/write [`AUPreset`](aupreset.md) data structure valid on the audio unit global scope, The `presetName` field in the struct is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) and follows Core Foundation memory semantics.

When setting the active factory preset on an audio unit with the [`AudioUnitSetProperty(_:_:_:_:_:_:)`](audiounitsetproperty(_:_:_:_:_:_:).md) function, you own the reference to the preset name and are responsible for later releasing it by calling the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function.

When obtaining the active factory preset from an audio unit with the [`AudioUnitGetProperty(_:_:_:_:_:_:)`](audiounitgetproperty(_:_:_:_:_:_:).md) function, you also own the reference to the preset name and are responsible for later releasing it by calling the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function.

## See Also

- [var kAudioUnitProperty_ElementCount: AudioUnitPropertyID](kaudiounitproperty_elementcount.md)
  A read/write `UInt32` value valid on any audio unit scope. The global audio unit scope always has an element count of 1.
- [var kAudioUnitProperty_SupportedNumChannels: AudioUnitPropertyID](kaudiounitproperty_supportednumchannels.md)
  A read-only array of channel information structures valid on the audio unit global scope.
- [var kAudioUnitProperty_AudioChannelLayout: AudioUnitPropertyID](kaudiounitproperty_audiochannellayout.md)
  A read/write `AudioChannelLayout` data structure valid on the audio unit input and output scopes.
- [var kAudioUnitProperty_AudioUnitMIDIProtocol: AudioUnitPropertyID](kaudiounitproperty_audiounitmidiprotocol.md)
- [var kAudioUnitProperty_AUHostIdentifier: AudioUnitPropertyID](kaudiounitproperty_auhostidentifier.md)
- [var kAudioUnitProperty_BypassEffect: AudioUnitPropertyID](kaudiounitproperty_bypasseffect.md)
  A read/write `UInt32` value, representing a Boolean value, valid on the audio unit global scope.
- [var kAudioUnitProperty_ClassInfo: AudioUnitPropertyID](kaudiounitproperty_classinfo.md)
  Describes the state of an audio unit.
- [var kAudioUnitProperty_ClassInfoFromDocument: AudioUnitPropertyID](kaudiounitproperty_classinfofromdocument.md)
  A read/write CFDictionary object, valid on the audio unit global scope.
- [var kAudioUnitProperty_CocoaUI: AudioUnitPropertyID](kaudiounitproperty_cocoaui.md)
  A read-only `AudioUnitCocoaViewInfo` data structure valid on the audio unit global scope.
- [var kAudioUnitProperty_ContextName: AudioUnitPropertyID](kaudiounitproperty_contextname.md)
- [var kAudioUnitProperty_CPULoad: AudioUnitPropertyID](kaudiounitproperty_cpuload.md)
  A read-only `Float64` value valid on the audio unit global scope.
- [var kAudioUnitProperty_DependentParameters: AudioUnitPropertyID](kaudiounitproperty_dependentparameters.md)
- [var kAudioUnitProperty_ElementName: AudioUnitPropertyID](kaudiounitproperty_elementname.md)
  The name of the specified element.
- [var kAudioUnitProperty_FactoryPresets: AudioUnitPropertyID](kaudiounitproperty_factorypresets.md)
  So-called  (as opposed to user-configured presets) are ones supplied with an audio unit by the manufacturer. You choose the active preset by setting the `kAudioUnitProperty_PresentPreset` property.
- [var kAudioUnitProperty_FastDispatch: AudioUnitPropertyID](kaudiounitproperty_fastdispatch.md)
  A read-only `void *` value valid on the audio unit global scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_presentpreset)*