# AudioComponentInstantiationOptions

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
struct AudioComponentInstantiationOptions
```

## Topics

### Constants
- [static var loadInProcess: AudioComponentInstantiationOptions](audiocomponentinstantiationoptions/loadinprocess.md)
- [static var loadOutOfProcess: AudioComponentInstantiationOptions](audiocomponentinstantiationoptions/loadoutofprocess.md)
### Initializers
- [init(rawValue: UInt32)](audiocomponentinstantiationoptions/init(rawvalue:).md)
### Type Properties
- [static var loadedRemotely: AudioComponentInstantiationOptions](audiocomponentinstantiationoptions/loadedremotely.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](audiocomponentinstancenew(_:_:).md)
  Creates a new instance of an audio component.
- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](audiocomponentinstantiate(_:_:_:).md)
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](audiocomponentinstancedispose(_:).md)
  Disposes of an audio component instance.
- [typealias AudioComponent](audiocomponent.md)
  An audio component.
- [Audio Component Errors](1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)*