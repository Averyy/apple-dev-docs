# AudioComponentCopyConfigurationInfo(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

## See Also

- [func AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Bool](audiocomponentinstancecando(_:_:).md)
  Determines if an audio component instance implements a particular function.
- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](audiocomponentgetdescription(_:_:).md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](audiocomponentcopyname(_:_:).md)
  Returns the generic name of an audio component.
- [func AudioComponentGetVersion(AudioComponent, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocomponentgetversion(_:_:).md)
  Gets the version of an audio component in hexadecimal form as `0xMMMMmmDD` (major, minor, dot).
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](audiocomponentcopyicon(_:).md)
- [struct AudioComponentPlugInInterface](audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentcopyconfigurationinfo(_:_:))*