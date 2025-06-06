# nextAvailableInputBus

**Framework**: AVFAudio  
**Kind**: property

An unused input bus.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var nextAvailableInputBus: AVAudioNodeBus { get }
```

#### Discussion

This method finds and returns the first input bus that doesn’t have a connection with a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentnode/nextavailableinputbus)*