# AudioComponentGetDescription(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets the class description, as an `AudioComponentDescription` structure, of an audio component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentGetDescription(_ inComponent: AudioComponent, _ outDesc: UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus
```

```c
extern OSStatus AudioComponentGetDescription(AudioComponent inComponent, AudioComponentDescription *outDesc);
```

## Return Value

A result code.

## Parameters

- `inComponent`: The audio component that you want a description of.
- `outDesc`: The description of the specified audio component.

## See Also

### Getting Information About a Component
- [func AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Bool](./audiocomponentinstancecando%28_,_%29.md)
  Determines if an audio component instance implements a particular function.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./audiocomponentcopyname%28_,_%29.md)
  Returns the generic name of an audio component.
- [func AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiocomponentgetversion%28_,_%29.md)
  Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](./audiocomponentcopyicon%28_%29.md)
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./audiocomponentcopyconfigurationinfo%28_,_%29.md)
- [struct AudioComponentPlugInInterface](./audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](./audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentgetdescription(_:_:))*