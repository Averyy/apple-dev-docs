# init(coder:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Tells you when to initialize a sprite from an archive.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init?(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Discussion

Don’t call this function directly; the system calls this function when you should initialize your sprite from the argument archived data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/init(coder:))*