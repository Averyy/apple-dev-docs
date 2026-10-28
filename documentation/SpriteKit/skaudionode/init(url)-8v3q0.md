# init(url:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

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
convenience init(url: URL)
```

```objc
- (instancetype) initWithURL:(NSURL *) url;
```

## Return Value

A newly initialized audio node.

## Parameters

- `url`: The URL of an audio file.

## See Also

### Initializing Audio Nodes
- [init(avAudioNode: AVAudioNode?)](./init%28avaudionode%29-969st.md)
  Initializes an audio node from an AVFoundation audio node.
- [convenience init(fileNamed: String)](./init%28filenamed%29.md)
  Initializes an audio node from an audio asset with the specified filename.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to initialize an audio node that has been unarchived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/init(url:)-8v3q0)*