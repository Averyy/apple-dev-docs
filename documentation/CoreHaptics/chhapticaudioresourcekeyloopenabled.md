# CHHapticAudioResourceKeyLoopEnabled

**Framework**: Core Haptics  
**Kind**: var  
**Role**: Global Variable

A key for a Boolean value that indicates whether to loop audio playback.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
let CHHapticAudioResourceKeyLoopEnabled: String
```

```c
extern CHHapticAudioResourceKey CHHapticAudioResourceKeyLoopEnabled;
```

## Discussion

Set a [`true`](../Swift/true.md) value for this key to loop the contents of an audio file.

The default value is [`false`](../Swift/false.md).

## See Also

### Audio Resource Keys
- [let CHHapticAudioResourceKeyUseVolumeEnvelope: String](./chhapticaudioresourcekeyusevolumeenvelope.md)
  A key for a Boolean value that indicates whether audio file playback fades in and out using an envelope.
- [typealias CHHapticAudioResourceKey](./chhapticaudioresourcekey.md)
  A type alias for a key that identifies the playback behavior of an audio resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticaudioresourcekeyloopenabled)*