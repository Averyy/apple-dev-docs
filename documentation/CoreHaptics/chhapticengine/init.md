# init()

**Framework**: Core Haptics  
**Kind**: init

Creates an instance of the haptic engine.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init() throws
```

#### Discussion

The haptic engine isn’t a singleton but a connection to the haptic server inside the user’s device. More than one connection with the haptic server may exist in your app’s view controller or delegate. Each connection functions independently of the others.

## See Also

- [init(audioSession: AVAudioSession?) throws](chhapticengine/init(audiosession:).md)
  Creates a haptic engine from an audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/init())*