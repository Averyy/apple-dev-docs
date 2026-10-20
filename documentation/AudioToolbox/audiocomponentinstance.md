# AudioComponentInstance

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A component instance, or object, is an audio unit or audio codec.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
typealias AudioComponentInstance = OpaquePointer
```

*macOS*

```swift
typealias AudioComponentInstance = UnsafeMutablePointer<ComponentInstanceRecord>
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```c
typedef struct OpaqueAudioComponentInstance * AudioComponentInstance;
```

*macOS*

```c
typedef struct ComponentInstanceRecord * AudioComponentInstance;
```

## See Also

### Creating an Audio Component Dynamically
- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](./audiocomponentregister%28_,_,_,_%29.md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](./audiocomponentcount%28_%29.md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](./audiocomponentfindnext%28_,_%29.md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](./audiocomponentinstancegetcomponent%28_%29.md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [struct AudioComponentDescription](./audiocomponentdescription.md)
  Identifying information for an audio component.
- [struct AudioComponentFlags](./audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](./audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstance)*