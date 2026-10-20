# style

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of the item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var style: UIBarButtonItem.Style { get set }
```

```objc
@property (nonatomic, assign, readwrite) UIBarButtonItemStyle style;
```

#### Discussion

One of the constants defined in [`UIBarButtonItem.Style`](./style-swift.enum.md). The default value is [`UIBarButtonItem.Style.plain`](./style-swift.enum/plain.md).

## See Also

### Customizing item appearance
- [UIBarButtonItem.Style](./style-swift.enum.md)
  Constants that specify the style of an item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/style-swift.property)*