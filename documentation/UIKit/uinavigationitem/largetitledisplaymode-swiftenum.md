# UINavigationItem.LargeTitleDisplayMode

**Framework**: UIKit  
**Kind**: enum

Constants that indicate how to size the title of this item.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum LargeTitleDisplayMode
```

## Topics

### Constants
- [UINavigationItem.LargeTitleDisplayMode.automatic](uinavigationitem/largetitledisplaymode-swift.enum/automatic.md)
  Inherit the display mode from the previous navigation item.
- [UINavigationItem.LargeTitleDisplayMode.always](uinavigationitem/largetitledisplaymode-swift.enum/always.md)
  Always display a large title.
- [UINavigationItem.LargeTitleDisplayMode.never](uinavigationitem/largetitledisplaymode-swift.enum/never.md)
  Never display a large title.
### Enumeration Cases
- [UINavigationItem.LargeTitleDisplayMode.inline](uinavigationitem/largetitledisplaymode-swift.enum/inline.md)
  Always use a large title when this item is topmost. If there is a back button present, this will revert to `Always`. Leading & center items will move to the overflow menu if present.
### Initializers
- [init?(rawValue: Int)](uinavigationitem/largetitledisplaymode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var title: String?](uinavigationitem/title.md)
  The navigation item’s title that displays in the navigation bar.
- [var attributedTitle: AttributedString?](uinavigationitem/attributedtitle-25fxb.md)
- [var largeTitle: String?](uinavigationitem/largetitle.md)
  String to be used as the large title.
- [var largeTitleDisplayMode: UINavigationItem.LargeTitleDisplayMode](uinavigationitem/largetitledisplaymode-swift.property.md)
  The mode for displaying the title of the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largetitledisplaymode-swift.enum)*