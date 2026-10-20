# AudioComponentCopyIcon(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func AudioComponentCopyIcon(_ comp: AudioComponent) -> UIImage?
```

*macOS*

```swift
func AudioComponentCopyIcon(_ comp: AudioComponent) -> NSImage?
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```c
extern UIImage *AudioComponentCopyIcon(AudioComponent comp);
```

*macOS*

```c
extern NSImage *AudioComponentCopyIcon(AudioComponent comp);
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
- [func AudioComponentCopyConfigurationInfo(AudioComponent, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> OSStatus](./audiocomponentcopyconfigurationinfo%28_,_%29.md)
- [struct AudioComponentPlugInInterface](./audiocomponentplugininterface.md)
- [typealias AudioComponentMethod](./audiocomponentmethod.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentcopyicon(_:))*