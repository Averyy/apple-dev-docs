# AudioComponentFindNext(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentFindNext(_ inComponent: AudioComponent?, _ inDesc: UnsafePointer<AudioComponentDescription>) -> AudioComponent?
```

```c
extern AudioComponentAudioComponentFindNext(AudioComponent inComponent, const AudioComponentDescription *inDesc);
```

#### Return Value

An audio component, or [`nil`](../ObjectiveC/nil-227m0.md) if not found.

## Parameters

- `inComponent`: The audio component that you want to start searching after.
- `inDesc`: The description of the audio component you want to find.

## See Also

### Creating an Audio Component Dynamically
- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](./audiocomponentregister%28_,_,_,_%29.md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](./audiocomponentcount%28_%29.md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](./audiocomponentinstancegetcomponent%28_%29.md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [struct AudioComponentDescription](./audiocomponentdescription.md)
  Identifying information for an audio component.
- [typealias AudioComponentInstance](./audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [struct AudioComponentFlags](./audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](./audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentfindnext(_:_:))*