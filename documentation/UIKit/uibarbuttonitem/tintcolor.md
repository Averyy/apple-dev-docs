# tintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tint color to apply to the button item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var tintColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * tintColor;
```

#### Discussion

In iOS 7 and later, all subclasses of [`UIView`](../uiview.md) derive their behavior for [`tintColor`](../uiview/tintcolor.md) from the base class. Although [`UIBarButtonItem`](../uibarbuttonitem.md) isn’t a view, its [`tintColor`](./tintcolor.md) property behaves the same as that of [`UIView`](../uiview.md). See the discussion of [`tintColor`](../uiview/tintcolor.md) in [`UIView`](../uiview.md) for more information.

## See Also

### Customizing item appearance
- [var style: UIBarButtonItem.Style](./style-swift.property.md)
  The style of the item.
- [UIBarButtonItem.Style](./style-swift.enum.md)
  Constants that specify the style of an item.
- [var isHidden: Bool](./ishidden.md)
  A Boolean that determines the visibility of the item.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the button is in a selected state.
- [var width: CGFloat](./width.md)
  The width of the item.
- [var possibleTitles: Set<String>?](./possibletitles.md)
  The set of possible titles to display on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor)*