# init(attributedText:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Initializes a new label object with an attributed text string.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(attributedText: NSAttributedString?)
```

```objc
+ (instancetype) labelNodeWithAttributedText:(NSAttributedString *) attributedText;
```

#### Return Value

A lable initialized from attributed text.

#### Discussion

## Parameters

- `attributedText`: The attributed string from which to initialize the label.

## See Also

### Creating a Label
- [init(fontNamed: String?)](./init%28fontnamed%29.md)
  Initializes a new label object with a specified font.
- [convenience init(text: String?)](./init%28text%29.md)
  Initializes a new label object with a text string.
- [+ labelNodeWithFontNamed:](./labelnodewithfontnamed_.md)
  Initializes a new label object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/init(attributedtext:))*