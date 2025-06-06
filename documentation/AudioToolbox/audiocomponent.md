# AudioComponent

**Framework**: Audio Toolbox  
**Kind**: typealias

An audio component.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioComponent = OpaquePointer
```

## See Also

- [func AudioComponentInstanceNew(AudioComponent, UnsafeMutablePointer<AudioComponentInstance?>) -> OSStatus](audiocomponentinstancenew(_:_:).md)
  Creates a new instance of an audio component.
- [func AudioComponentInstantiate(AudioComponent, AudioComponentInstantiationOptions, (AudioComponentInstance?, OSStatus) -> Void)](audiocomponentinstantiate(_:_:_:).md)
- [func AudioComponentInstanceDispose(AudioComponentInstance) -> OSStatus](audiocomponentinstancedispose(_:).md)
  Disposes of an audio component instance.
- [struct AudioComponentInstantiationOptions](audiocomponentinstantiationoptions.md)
- [Audio Component Errors](1619490-audio-component-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponent)*