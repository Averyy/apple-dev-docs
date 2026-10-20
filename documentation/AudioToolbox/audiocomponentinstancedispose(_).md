# AudioComponentInstanceDispose(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Disposes of an audio component instance.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentInstanceDispose(_ inInstance: AudioComponentInstance) -> OSStatus
```

```c
extern OSStatus AudioComponentInstanceDispose(AudioComponentInstance inInstance);
```

#### Return Value

A result code.

## Parameters

- `inInstance`: The audio component instance that you want to dispose of.

## See Also

### Creating an Audio Component Instance
- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](./audiocomponentinstancenew%28_,_%29.md)
  Creates a new instance of an audio component.
- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](./audiocomponentinstantiate%28_,_,_%29.md)
- [typealias AudioComponent](./audiocomponent.md)
  An audio component.
- [struct AudioComponentInstantiationOptions](./audiocomponentinstantiationoptions.md)
- [Audio Component Errors](./api-1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstancedispose(_:))*