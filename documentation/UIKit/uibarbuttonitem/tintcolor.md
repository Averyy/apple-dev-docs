# tintColor

**Framework**: UIKit  
**Kind**: property

The tint color to apply to the button item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var tintColor: UIColor? { get set }
```

#### Discussion

In iOS 7 and later, all subclasses of [`UIView`](uiview.md) derive their behavior for [`tintColor`](uiview/tintcolor.md) from the base class. Although [`UIBarButtonItem`](uibarbuttonitem.md) isn’t a view, its [`tintColor`](uibarbuttonitem/tintcolor.md) property behaves the same as that of [`UIView`](uiview.md). See the discussion of [`tintColor`](uiview/tintcolor.md) in [`UIView`](uiview.md) for more information.

## See Also

- [var style: UIBarButtonItem.Style](uibarbuttonitem/style-swift.property.md)
  The style of the item.
- [UIBarButtonItem.Style](uibarbuttonitem/style-swift.enum.md)
  Constants that specify the style of an item.
- [var isHidden: Bool](uibarbuttonitem/ishidden.md)
  A Boolean that determines the visibility of the item.
- [var isSelected: Bool](uibarbuttonitem/isselected.md)
  A Boolean value that indicates whether the button is in a selected state.
- [var width: CGFloat](uibarbuttonitem/width.md)
  The width of the item.
- [var possibleTitles: Set<String>?](uibarbuttonitem/possibletitles.md)
  The set of possible titles to display on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/tintcolor)*