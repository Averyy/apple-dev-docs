# AudioComponentInstantiationOptions

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
struct AudioComponentInstantiationOptions
```

```c
enum AudioComponentInstantiationOptions : UInt32;
```

## Topics

### Constants
- [static var loadInProcess: AudioComponentInstantiationOptions](./audiocomponentinstantiationoptions/loadinprocess.md)
- [static var loadOutOfProcess: AudioComponentInstantiationOptions](./audiocomponentinstantiationoptions/loadoutofprocess.md)
### Initializers
- [init(rawValue: UInt32)](./audiocomponentinstantiationoptions/init%28rawvalue%29.md)
### Type Properties
- [static var loadedRemotely: AudioComponentInstantiationOptions](./audiocomponentinstantiationoptions/loadedremotely.md)

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

### Creating an Audio Component Instance
- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](./audiocomponentinstancenew%28_,_%29.md)
  Creates a new instance of an audio component.
- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](./audiocomponentinstantiate%28_,_,_%29.md)
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](./audiocomponentinstancedispose%28_%29.md)
  Disposes of an audio component instance.
- [typealias AudioComponent](./audiocomponent.md)
  An audio component.
- [Audio Component Errors](./api-1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiationoptions)*