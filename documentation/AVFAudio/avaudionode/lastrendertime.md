# lastRenderTime

**Framework**: AVFAudio  
**Kind**: property

The most recent render time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lastRenderTime: AVAudioTime? { get }
```

#### Discussion

This value is `nil` if the engine isn’t running or if you don’t connect the node to an input or output node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/lastrendertime)*