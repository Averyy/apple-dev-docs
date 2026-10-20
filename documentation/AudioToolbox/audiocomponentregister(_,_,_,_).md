# AudioComponentRegister(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentRegister(_ inDesc: UnsafePointer<AudioComponentDescription>, _ inName: CFString, _ inVersion: UInt32, _ inFactory: AudioComponentFactoryFunction) -> AudioComponent
```

```c
extern AudioComponentAudioComponentRegister(const AudioComponentDescription *inDesc, CFStringRef inName, UInt32 inVersion, AudioComponentFactoryFunction inFactory);
```

## See Also

### Creating an Audio Component Dynamically
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](./audiocomponentcount%28_%29.md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](./audiocomponentfindnext%28_,_%29.md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](./audiocomponentinstancegetcomponent%28_%29.md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [struct AudioComponentDescription](./audiocomponentdescription.md)
  Identifying information for an audio component.
- [typealias AudioComponentInstance](./audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [struct AudioComponentFlags](./audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](./audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentregister(_:_:_:_:))*