# attributedText

**Framework**: SpriteKit  
**Kind**: property

The attributed string displayed by the label.

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
@NSCopying
@MainActor var attributedText: NSAttributedString? { get set }
```

#### Discussion

The following properties are ignored if attributedText is defined:

| text | The label favors the attributed string. |
| --- | --- |
| fontColor | Font color is defined by tags in the attributed string. |
| fontSize | Font size is defined by tags in the attributed string. |

## See Also

- [var text: String?](sklabelnode/text.md)
  The string that the label node displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/attributedtext)*