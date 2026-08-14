# AudioComponentFlags

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
struct AudioComponentFlags
```

## Topics

### Flags
- [static var unsearchable: AudioComponentFlags](audiocomponentflags/unsearchable.md)
- [static var sandboxSafe: AudioComponentFlags](audiocomponentflags/sandboxsafe.md)
- [static var isV3AudioUnit: AudioComponentFlags](audiocomponentflags/isv3audiounit.md)
- [static var requiresAsyncInstantiation: AudioComponentFlags](audiocomponentflags/requiresasyncinstantiation.md)
- [static var canLoadInProcess: AudioComponentFlags](audiocomponentflags/canloadinprocess.md)
### Initializers
- [init(rawValue: UInt32)](audiocomponentflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](audiocomponentregister(_:_:_:_:).md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](audiocomponentcount(_:).md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](audiocomponentfindnext(_:_:).md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](audiocomponentinstancegetcomponent(_:).md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [struct AudioComponentDescription](audiocomponentdescription.md)
  Identifying information for an audio component.
- [typealias AudioComponentInstance](audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [typealias AudioComponentFactoryFunction](audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentflags)*