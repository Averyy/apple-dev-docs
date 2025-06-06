# init(node:bus:)

**Framework**: AVFAudio  
**Kind**: init

Creates a connection point object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(node: AVAudioNode, bus: AVAudioNodeBus)
```

#### Discussion

If the node is `nil`, this method fails and returns `nil`.

## Parameters

- `node`: The source or destination node.
- `bus`: The output or input bus on the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconnectionpoint/init(node:bus:))*