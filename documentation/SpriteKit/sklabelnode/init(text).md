# init(text:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new label object with a text string.

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
convenience init(text: String?)
```

```objc
+ (instancetype) labelNodeWithText:(NSString *) text;
```

#### Return Value

An initialized label object.

#### Discussion

The label node’s font is set to Helvetica Neue Ultra Light, 32 point.

## Parameters

- `text`: The text to use to initialize the label node.

## See Also

### Creating a Label
- [init(fontNamed: String?)](./init%28fontnamed%29.md)
  Initializes a new label object with a specified font.
- [convenience init(attributedText: NSAttributedString?)](./init%28attributedtext%29.md)
  Initializes a new label object with an attributed text string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/init(text:))*