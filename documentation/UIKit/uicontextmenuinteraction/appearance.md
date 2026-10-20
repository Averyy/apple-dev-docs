# UIContextMenuInteraction.appearance

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the appearance of the menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum appearance
```

```c
enum UIContextMenuInteractionAppearance : NSInteger;
```

## Topics

### Constants
- [UIContextMenuInteraction.appearance.unknown](./appearance/unknown.md)
  No menu appearance.
- [UIContextMenuInteraction.appearance.rich](./appearance/rich.md)
  A modal menu with an optional preview.
- [UIContextMenuInteraction.appearance.compact](./appearance/compact.md)
  A nonmodal, compact menu with no preview.
### Initializers
- [init?(rawValue: Int)](./appearance/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the menu appearance
- [var menuAppearance: UIContextMenuInteraction.appearance](./menuappearance.md)
  The appearance of the context menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/appearance)*