# CHHapticAudioResourceID

**Framework**: Core Haptics  
**Kind**: typealias  
**Role**: Type Alias

A type that identifies a custom audio resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias CHHapticAudioResourceID = Int
```

```c
typedef NSUInteger CHHapticAudioResourceID;
```

## See Also

### Registering Audio Resources
- [func registerAudioResource(URL, options: [AnyHashable : Any]) throws -> CHHapticAudioResourceID](./chhapticengine/registeraudioresource%28_,options%29.md)
  Registers an external audio to use as a custom waveform.
- [func unregisterAudioResource(CHHapticAudioResourceID) throws](./chhapticengine/unregisteraudioresource%28_%29.md)
  Unregisters an external audio file that you previously registered with the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourceid)*