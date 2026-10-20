# UIBarButtonItem.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the style of an item.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
enum Style
```

```c
enum UIBarButtonItemStyle : NSInteger;
```

## Topics

### Constants
- [UIBarButtonItem.Style.plain](./style-swift.enum/plain.md)
  A button style with plain text styling.
- [UIBarButtonItem.Style.prominent](./style-swift.enum/prominent.md)
  A button item style for a prominent button.
- [UIBarButtonItem.Style.bordered](./style-swift.enum/bordered.md)
  A simple button style with a border.
- [static var done: UIBarButtonItem.Style](./style-swift.enum/done.md)
  A button style for a done button.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing item appearance
- [var style: UIBarButtonItem.Style](./style-swift.property.md)
  The style of the item.
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the button item.
- [var isHidden: Bool](./ishidden.md)
  A Boolean that determines the visibility of the item.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the button is in a selected state.
- [var width: CGFloat](./width.md)
  The width of the item.
- [var possibleTitles: Set<String>?](./possibletitles.md)
  The set of possible titles to display on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/style-swift.enum)*