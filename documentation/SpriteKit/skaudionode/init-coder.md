# init(coder:)

**Framework**: SpriteKit  
**Kind**: init

Tells you when to initialize an audio node that has been unarchived.

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
@MainActor
init?(coder aDecoder: NSCoder)
```

#### Discussion

Do not call this initializer directly; it’s called by the system when you should initialize an audio node that has been unarchived.

## See Also

- [init(avAudioNode: AVAudioNode?)](skaudionode/init(avaudionode:).md)
  Initializes an audio node from an AVFoundation audio node.
- [convenience init(fileNamed: String)](skaudionode/init(filenamed:).md)
  Initializes an audio node from an audio asset with the specified filename.
- [convenience init(url: URL)](skaudionode/init(url:).md)
  Initializes an audio node from an audio asset with the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/init(coder:))*