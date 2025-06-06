# AudioComponentPlugInInterface

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioComponentPlugInInterface
```

## Topics

### Initializers
- [init(Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus, Close: (UnsafeMutableRawPointer) -> OSStatus, Lookup: (Int16) -> AudioComponentMethod?, reserved: UnsafeMutableRawPointer?)](audiocomponentplugininterface/init(open:close:lookup:reserved:)-1bmzd.md)
- [init(Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus, Close: (UnsafeMutableRawPointer) -> OSStatus, Lookup: (Int16) -> AudioComponentMethod?, reserved: UnsafeMutableRawPointer?)](audiocomponentplugininterface/init(open:close:lookup:reserved:)-1hqa3.md)
### Instance Properties
- [var Close: (UnsafeMutableRawPointer) -> OSStatus](audiocomponentplugininterface/close.md)
- [var Lookup: (Int16) -> AudioComponentMethod?](audiocomponentplugininterface/lookup.md)
- [var Open: (UnsafeMutableRawPointer, AudioComponentInstance) -> OSStatus](audiocomponentplugininterface/open.md)
- [var reserved: UnsafeMutableRawPointer?](audiocomponentplugininterface/reserved.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](audiocomponentcopyconfigurationinfo(_:_:).md)
- [typealias AudioComponentMethod](audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentplugininterface)*