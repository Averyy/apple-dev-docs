# width

**Framework**: UIKit  
**Kind**: property

The width of the item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var width: CGFloat { get set }
```

#### Discussion

If this property value is positive, the width of the combined image and title are fixed. If the value is `0.0` or negative, the item sets the width of the combined image and title to fit. This property is ignored if the style uses radio mode. The default value is `0.0`.

## See Also

- [var style: UIBarButtonItem.Style](uibarbuttonitem/style-swift.property.md)
  The style of the item.
- [UIBarButtonItem.Style](uibarbuttonitem/style-swift.enum.md)
  Constants that specify the style of an item.
- [var tintColor: UIColor?](uibarbuttonitem/tintcolor.md)
  The tint color to apply to the button item.
- [var isHidden: Bool](uibarbuttonitem/ishidden.md)
  A Boolean that determines the visibility of the item.
- [var isSelected: Bool](uibarbuttonitem/isselected.md)
  A Boolean value that indicates whether the button is in a selected state.
- [var possibleTitles: Set<String>?](uibarbuttonitem/possibletitles.md)
  The set of possible titles to display on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/width)*