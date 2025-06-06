# unregisterAudioResource(_:)

**Framework**: Core Haptics  
**Kind**: method

Unregisters an external audio file that you previously registered with the engine.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func unregisterAudioResource(_ resourceID: CHHapticAudioResourceID) throws
```

## Parameters

- `resourceID`: The ID of the audio resource you’d like to unregister.

## See Also

- [func registerAudioResource(URL, options: [AnyHashable : Any]) throws -> CHHapticAudioResourceID](chhapticengine/registeraudioresource(_:options:).md)
  Registers an external audio to use as a custom waveform.
- [typealias CHHapticAudioResourceID](chhapticaudioresourceid.md)
  A type that identifies a custom audio resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/unregisteraudioresource(_:))*