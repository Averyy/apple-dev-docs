# AudioComponentInstanceCanDo(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

## Parameters

- `inInstance`: The audio component instance that you want to examine.
- `inSelectorID`: An audio component function selector. The available values for audio units are listed in   and  .

## See Also

- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](audiocomponentgetdescription(_:_:).md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](audiocomponentcopyname(_:_:).md)
  Returns the generic name of an audio component.
- [func AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocomponentgetversion(_:_:).md)
  Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](audiocomponentcopyicon(_:).md)
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](audiocomponentcopyconfigurationinfo(_:_:).md)
- [struct AudioComponentPlugInInterface](audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstancecando(_:_:))*