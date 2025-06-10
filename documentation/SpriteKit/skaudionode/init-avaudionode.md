# init(avAudioNode:)

**Framework**: SpriteKit  
**Kind**: init

Initializes an audio node from an AVFoundation audio node.

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
init(avAudioNode node: AVAudioNode?)
```

#### Return Value

A newly initialized audio node.

## Parameters

- `node`: An   object that holds an   sound graph from a single sound source or URL.

## See Also

- [convenience init(fileNamed: String)](skaudionode/init(filenamed:).md)
  Initializes an audio node from an audio asset with the specified filename.
- [convenience init(url: URL)](skaudionode/init(url:).md)
  Initializes an audio node from an audio asset with the specified URL.
- [init?(coder: NSCoder)](skaudionode/init(coder:).md)
  Tells you when to initialize an audio node that has been unarchived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/init(avaudionode:))*