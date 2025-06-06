# AudioComponentGetVersion(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

#### Return Value

A result code.

## Parameters

- `inComponent`: The audio component that you want the version of.
- `outVersion`: The version of the specified audio component.

## See Also

- [func AudioComponentInstanceCanDo(AudioComponentInstance, Int16) -> Bool](audiocomponentinstancecando(_:_:).md)
  Determines if an audio component instance implements a particular function.
- [func AudioComponentGetDescription(AudioComponent, UnsafeMutablePointer<AudioComponentDescription>) -> OSStatus](audiocomponentgetdescription(_:_:).md)
  Gets the class description, as an `AudioComponentDescription` structure, of an audio component.
- [func AudioComponentCopyName(AudioComponent, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](audiocomponentcopyname(_:_:).md)
  Returns the generic name of an audio component.
- [func AudioComponentCopyIcon(AudioComponent) -> UIImage?](audiocomponentcopyicon(_:).md)
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](audiocomponentcopyconfigurationinfo(_:_:).md)
- [struct AudioComponentPlugInInterface](audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentgetversion(_:_:))*