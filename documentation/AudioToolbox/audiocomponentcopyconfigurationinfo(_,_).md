# AudioComponentCopyConfigurationInfo(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentCopyConfigurationInfo(_ inComponent: AudioComponent, _ outConfigurationInfo: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus
```

```c
extern OSStatus AudioComponentCopyConfigurationInfo(AudioComponent inComponent, CFDictionaryRef*outConfigurationInfo);
```

## See Also

### Getting Information About a Component
- [func AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Bool](./audiocomponentinstancecando%28_,_%29.md)
  Determines if an audio component instance implements a particular function.
- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](./audiocomponentgetdescription%28_,_%29.md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./audiocomponentcopyname%28_,_%29.md)
  Returns the generic name of an audio component.
- [func AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiocomponentgetversion%28_,_%29.md)
  Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](./audiocomponentcopyicon%28_%29.md)
- [struct AudioComponentPlugInInterface](./audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](./audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentcopyconfigurationinfo(_:_:))*