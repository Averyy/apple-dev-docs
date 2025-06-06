# registerAudioResource(_:options:)

**Framework**: Corehaptics  
**Kind**: method

Registers an external audio to use as a custom waveform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func registerAudioResource(_ resourceURL: URL, options: [AnyHashable : Any] = [:]) throws -> CHHapticAudioResourceID
```

## Mentions

- [Preparing your app to play haptics](preparing-your-app-to-play-haptics.md)

#### Return Value

An identifier for the audio resource.

#### Discussion

Before you initialize a Core Haptics event with your own audio file, use this method to register the file with the engine. Reference external audio files using a URL.

Input the value that this method returns when creating the dictionary or event representation of a haptic pattern.

> **Note**:  In an Apple Haptics and Audio File (AHAP), you specify audio files by their path, as opposed to their registered resource URL. For more information, see [`Representing haptic patterns in AHAP files`](representing-haptic-patterns-in-ahap-files.md).

## Parameters

- `resourceURL`: A URL that identifies the location of the audio file to register.
- `options`: A dictionary with audio resource keys and values that describe how to play this resource.

## Topics

### Audio Resource Keys
- [let CHHapticAudioResourceKeyLoopEnabled: String](chhapticaudioresourcekeyloopenabled.md)
  A key for a Boolean value that indicates whether to loop audio playback.
- [let CHHapticAudioResourceKeyUseVolumeEnvelope: String](chhapticaudioresourcekeyusevolumeenvelope.md)
  A key for a Boolean value that indicates whether audio file playback fades in and out using an envelope.
- [typealias CHHapticAudioResourceKey](chhapticaudioresourcekey.md)
  A type alias for a key that identifies the playback behavior of an audio resource.

## See Also

- [func unregisterAudioResource(CHHapticAudioResourceID) throws](chhapticengine/unregisteraudioresource(_:).md)
  Unregisters an external audio file that you previously registered with the engine.
- [typealias CHHapticAudioResourceID](chhapticaudioresourceid.md)
  A type that identifies a custom audio resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/registeraudioresource(_:options:))*