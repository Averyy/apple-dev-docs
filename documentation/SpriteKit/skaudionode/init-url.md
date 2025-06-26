# init(url:)

**Framework**: SpriteKit  
**Kind**: init

Initializes an audio node from an audio asset with the specified URL.

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
convenience init(url: URL)
```

#### Return Value

A newly initialized audio node.

## Parameters

- `url`: The URL of an audio file.

## See Also

- [init(avAudioNode: AVAudioNode?)](skaudionode/init(avaudionode:).md)
  Initializes an audio node from an AVFoundation audio node.
- [convenience init(fileNamed: String)](skaudionode/init(filenamed:).md)
  Initializes an audio node from an audio asset with the specified filename.
- [init?(coder: NSCoder)](skaudionode/init(coder:).md)
  Tells you when to initialize an audio node that has been unarchived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/init(url:))*