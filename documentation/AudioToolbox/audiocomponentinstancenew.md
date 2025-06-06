# AudioComponentInstanceNew(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a new instance of an audio component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentInstanceNew(_ inComponent: AudioComponent, _ outInstance: UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus
```

## Mentions

- [Hosting Audio Unit Extensions Using the AUv2 API](hosting-audio-unit-extensions-using-the-auv2-api.md)

#### Return Value

A result code.

## Parameters

- `inComponent`: The audio component that you want to create a new instance of.
- `outInstance`: On output, the new audio component instance.

## See Also

- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](audiocomponentinstantiate(_:_:_:).md)
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](audiocomponentinstancedispose(_:).md)
  Disposes of an audio component instance.
- [typealias AudioComponent](audiocomponent.md)
  An audio component.
- [struct AudioComponentInstantiationOptions](audiocomponentinstantiationoptions.md)
- [Audio Component Errors](1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstancenew(_:_:))*