# AudioComponentPlugInInterface

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioComponentPlugInInterface
```

```c
struct AudioComponentPlugInInterface;
```

## Topics

### Initializers
- [init(Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus, Close: (UnsafeMutableRawPointer) -> OSStatus, Lookup: (Int16) -> AudioComponentMethod?, reserved: UnsafeMutableRawPointer?)](./audiocomponentplugininterface/init%28open,close,lookup,reserved%29-1bmzd.md)
- [init(Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus, Close: (UnsafeMutableRawPointer) -> OSStatus, Lookup: (Int16) -> AudioComponentMethod?, reserved: UnsafeMutableRawPointer?)](./audiocomponentplugininterface/init%28open,close,lookup,reserved%29-1hqa3.md)
### Instance Properties
- [var Close: (UnsafeMutableRawPointer) -> OSStatus](./audiocomponentplugininterface/close.md)
- [var Lookup: (Int16) -> AudioComponentMethod?](./audiocomponentplugininterface/lookup.md)
- [var Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus](./audiocomponentplugininterface/open.md)
- [var reserved: UnsafeMutableRawPointer?](./audiocomponentplugininterface/reserved.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

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
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./audiocomponentcopyconfigurationinfo%28_,_%29.md)
- [typealias AudioComponentMethod](./audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface)*