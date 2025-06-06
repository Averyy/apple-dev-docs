# possibleTitles

**Framework**: UIKit  
**Kind**: property

The set of possible titles to display on the bar button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var possibleTitles: Set<String>? { get set }
```

#### Discussion

Use this property to provide a hint to the system on how to correctly size the bar button item to be wide enough to accommodate your widest title. Set the value of this property to an [`NSSet`](https://developer.apple.com/documentation/Foundation/NSSet) object containing all the titles you intend as possible titles for the bar button item. Use the actual text strings you intend to display.

This property applies to bar button items placed on navigation bars or toolbars.

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
- [var width: CGFloat](uibarbuttonitem/width.md)
  The width of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/possibletitles)*