# UINavigationItem.LargeTitleDisplayMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how to size the title of this item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum LargeTitleDisplayMode
```

```c
enum UINavigationItemLargeTitleDisplayMode : NSInteger;
```

## Topics

### Constants
- [UINavigationItem.LargeTitleDisplayMode.automatic](./largetitledisplaymode-swift.enum/automatic.md)
  Inherit the display mode from the previous navigation item.
- [UINavigationItem.LargeTitleDisplayMode.always](./largetitledisplaymode-swift.enum/always.md)
  Always display a large title.
- [UINavigationItem.LargeTitleDisplayMode.never](./largetitledisplaymode-swift.enum/never.md)
  Never display a large title.
### Enumeration Cases
- [UINavigationItem.LargeTitleDisplayMode.inline](./largetitledisplaymode-swift.enum/inline.md)
  Always use a large title when this item is topmost. If there is a back button present, this will revert to `Always`. Leading & center items will move to the overflow menu if present.
### Initializers
- [init?(rawValue: Int)](./largetitledisplaymode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the title
- [var title: String?](./title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](./attributedtitle-25fxb.md)
  An attributed string that the system renders as the title in the navigation bar.
- [var largeTitle: String?](./largetitle.md)
  String to be used as the large title.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.
- [attributedTitle](./attributedtitle-9l8p2.md)
  An attributed string that is rendered as the title in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.enum)*