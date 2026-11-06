# UINavigationItem.TitleAlignment

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.2+
- iPadOS 27.2+
- Mac Catalyst 27.2+
- tvOS 27.2+
- visionOS 27.2+

## Declaration

```swift
enum TitleAlignment
```

```c
enum UINavigationItemTitleAlignment : NSInteger;
```

## Topics

### Getting title alignment options
- [UINavigationItem.TitleAlignment.automatic](./titlealignment-swift.enum/automatic.md)
  The system determines the alignment.
- [UINavigationItem.TitleAlignment.center](./titlealignment-swift.enum/center.md)
  The title is center-aligned.
- [UINavigationItem.TitleAlignment.leading](./titlealignment-swift.enum/leading.md)
  The title is leading-aligned.
### Initializers
- [init?(rawValue: Int)](./titlealignment-swift.enum/init%28rawvalue%29.md)

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
- [UINavigationItem.LargeTitleDisplayMode](./largetitledisplaymode-swift.enum.md)
  Constants that indicate how to size the title of this item.
- [var titleAlignment: UINavigationItem.TitleAlignment](./titlealignment-swift.property.md)
  The preferred alignment of the navigation bar’s title.
- [attributedTitle](./attributedtitle-9l8p2.md)
  An attributed string that is rendered as the title in the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/titlealignment-swift.enum)*