# AudioComponentFlags

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
struct AudioComponentFlags
```

```c
enum AudioComponentFlags : UInt32;
```

## Topics

### Flags
- [static var unsearchable: AudioComponentFlags](./audiocomponentflags/unsearchable.md)
- [static var sandboxSafe: AudioComponentFlags](./audiocomponentflags/sandboxsafe.md)
- [static var isV3AudioUnit: AudioComponentFlags](./audiocomponentflags/isv3audiounit.md)
- [static var requiresAsyncInstantiation: AudioComponentFlags](./audiocomponentflags/requiresasyncinstantiation.md)
- [static var canLoadInProcess: AudioComponentFlags](./audiocomponentflags/canloadinprocess.md)
### Initializers
- [init(rawValue: UInt32)](./audiocomponentflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

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
- [typealias AudioComponentInstance](./audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [typealias AudioComponentFactoryFunction](./audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)*