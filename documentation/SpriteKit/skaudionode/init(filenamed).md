# init(fileNamed:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes an audio node from an audio asset with the specified filename.

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
convenience init(fileNamed name: String)
```

```objc
- (instancetype) initWithFileNamed:(NSString *) name;
```

## Return Value

A newly initialized audio node.

## Discussion

The named file containing the audio asset must reside within the main bundle.

## Parameters

- `name`: A file containing an [`AVAudioNode`](../../AVFAudio/avaudionode.md).

## See Also

### Initializing Audio Nodes
- [init(avAudioNode: AVAudioNode?)](./init%28avaudionode%29-969st.md)
  Initializes an audio node from an AVFoundation audio node.
- [convenience init(url: URL)](./init%28url%29-8v3q0.md)
  Initializes an audio node from an audio asset with the specified URL.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Tells you when to initialize an audio node that has been unarchived.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaudionode/init(filenamed:))*