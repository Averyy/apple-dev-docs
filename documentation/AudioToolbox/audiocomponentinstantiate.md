# AudioComponentInstantiate(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentInstantiate(_ inComponent: AudioComponent, _ inOptions: AudioComponentInstantiationOptions, _ inCompletionHandler: @escaping (AudioComponentInstance?, OSStatus) -> Void)
```

## Mentions

- [Hosting Audio Unit Extensions Using the AUv2 API](hosting-audio-unit-extensions-using-the-auv2-api.md)

## See Also

- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](audiocomponentinstancenew(_:_:).md)
  Creates a new instance of an audio component.
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](audiocomponentinstancedispose(_:).md)
  Disposes of an audio component instance.
- [typealias AudioComponent](audiocomponent.md)
  An audio component.
- [struct AudioComponentInstantiationOptions](audiocomponentinstantiationoptions.md)
- [Audio Component Errors](1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstantiate(_:_:_:))*