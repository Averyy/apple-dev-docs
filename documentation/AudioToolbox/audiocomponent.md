# AudioComponent

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

An audio component.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioComponent = OpaquePointer
```

```c
typedef struct OpaqueAudioComponent * AudioComponent;
```

## See Also

### Creating an Audio Component Instance
- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](./audiocomponentinstancenew%28_,_%29.md)
  Creates a new instance of an audio component.
- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](./audiocomponentinstantiate%28_,_,_%29.md)
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](./audiocomponentinstancedispose%28_%29.md)
  Disposes of an audio component instance.
- [struct AudioComponentInstantiationOptions](./audiocomponentinstantiationoptions.md)
- [Audio Component Errors](./api-1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponent)*