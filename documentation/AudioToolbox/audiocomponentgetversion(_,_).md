# AudioComponentGetVersion(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentGetVersion(_ inComponent: AudioComponent, _ outVersion: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioComponentGetVersion(AudioComponent inComponent, UInt32 *outVersion);
```

## Return Value

A result code.

## Parameters

- `inComponent`: The audio component that you want the version of.
- `outVersion`: The version of the specified audio component.

## See Also

### Getting Information About a Component
- [func AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Bool](./audiocomponentinstancecando%28_,_%29.md)
  Determines if an audio component instance implements a particular function.
- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](./audiocomponentgetdescription%28_,_%29.md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./audiocomponentcopyname%28_,_%29.md)
  Returns the generic name of an audio component.
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](./audiocomponentcopyicon%28_%29.md)
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./audiocomponentcopyconfigurationinfo%28_,_%29.md)
- [struct AudioComponentPlugInInterface](./audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](./audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentgetversion(_:_:))*