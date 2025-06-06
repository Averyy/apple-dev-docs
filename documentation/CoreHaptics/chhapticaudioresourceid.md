# CHHapticAudioResourceID

**Framework**: Core Haptics  
**Kind**: typealias

A type that identifies a custom audio resource.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS ?+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
typealias CHHapticAudioResourceID = Int
```

## See Also

- [func registerAudioResource(URL, options: [AnyHashable : Any]) throws -> CHHapticAudioResourceID](chhapticengine/registeraudioresource(_:options:).md)
  Registers an external audio to use as a custom waveform.
- [func unregisterAudioResource(CHHapticAudioResourceID) throws](chhapticengine/unregisteraudioresource(_:).md)
  Unregisters an external audio file that you previously registered with the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourceid)*