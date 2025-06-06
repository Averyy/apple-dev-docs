# kAudioUnitProperty_ParameterStringFromValue

**Framework**: Audio Toolbox  
**Kind**: var

A read-only [`AudioUnitParameterStringFromValue`](audiounitparameterstringfromvalue.md) struct, valid on any audio unit scope.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioUnitProperty_ParameterStringFromValue: AudioUnitPropertyID { get }
```

#### Discussion

This property is used with parameters that are marked with the kAudioUnitParameterFlag_HasName parameter info flag. This indicates that some (or all) of the values represented by the parameter can and should be represented by a special display string.

This is NOT to be confused with kAudioUnitProperty_ParameterValueStrings. That property is used with parameters that are indexed and is typically used for instance to build a menu item of choices for one of several parameter values.

kAudioUnitProperty_ParameterStringFromValue can have a continuous range, and merely states to the host that if it is displaying those parameter’s values, they should request a name any time any value of the parameter is set when displaying that parameter.

For instance (a trivial example), a unit may present a gain parameter in a dB scale, and wish to display its minimum value as “negative infinity”. In this case, the audio unit will not return names for any parameter value greater than its minimum value - so the host will then just display the parameter value as is. For values less than or equal to the minimum value, the audio unit will return a string for “negative infinity” which the host can use to display appropriately.

A less trivial example might be a parameter that presents its values as seconds. However, in some situations this value should be better displayed in a SMPTE style of display.

```objc
HH:MM:SS:FF
```

In this case, the audio unit would return a name for any value of the parameter.

The GetProperty call is used in the same scope and element as the inParamID that is declared in the struct passed in to this property.

If the *inValue member is NULL, then the audio unit should take the current value of the specified parameter. If the *inValue member is NOT NULL, then the audio unit should return the name used for the specified value.

On exit, the outName may point to a CFStringRef (which if so must be released by the caller). If the parameter has no special name that should be applied to that parameter value, then outName will be NULL, and the host should display the parameter value as appropriate.

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiounitproperty_parameterstringfromvalue)*