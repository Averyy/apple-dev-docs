# AudioComponentInstanceCanDo(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Determines if an audio component instance implements a particular function.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentInstanceCanDo(_ inInstance: AudioComponentInstance, _ inSelectorID: Int16) -> Bool
```

```c
extern Boolean AudioComponentInstanceCanDo(AudioComponentInstance inInstance, SInt16 inSelectorID);
```

## Parameters

- `inInstance`: The audio component instance that you want to examine.
- `inSelectorID`: An audio component function selector. The available values for audio units are listed in [General Audio Unit Function Selectors](./api-1584140-general_audio_unit_function_sele.md) and [I/O Audio Unit Function Selectors](./api-1585807-i_o_audio_unit_function_selector.md).

## See Also

### Getting Information About a Component
- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](./audiocomponentgetdescription%28_,_%29.md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./audiocomponentcopyname%28_,_%29.md)
  Returns the generic name of an audio component.
- [func AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiocomponentgetversion%28_,_%29.md)
  Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](./audiocomponentcopyicon%28_%29.md)
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./audiocomponentcopyconfigurationinfo%28_,_%29.md)
- [struct AudioComponentPlugInInterface](./audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](./audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstancecando(_:_:))*