# UIContextMenuInteractionCommitStyle

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that control the interaction commit style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UIContextMenuInteractionCommitStyle
```

```c
enum UIContextMenuInteractionCommitStyle : NSInteger;
```

## Topics

### Interaction Styles
- [UIContextMenuInteractionCommitStyle.dismiss](./uicontextmenuinteractioncommitstyle/dismiss.md)
  An interaction with no animations.
- [UIContextMenuInteractionCommitStyle.pop](./uicontextmenuinteractioncommitstyle/pop.md)
  An interaction that uses animations.
### Initializers
- [init?(rawValue: Int)](./uicontextmenuinteractioncommitstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Specifying the Commit Style
- [var preferredCommitStyle: UIContextMenuInteractionCommitStyle](./uicontextmenuinteractioncommitanimating/preferredcommitstyle.md)
  The preferred animation style triggered when the user taps the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteractioncommitstyle)*