# possibleTitles

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The set of possible titles to display on the bar button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var possibleTitles: Set<String>? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSSet<NSString *> * possibleTitles;
```

#### Discussion

Use this property to provide a hint to the system on how to correctly size the bar button item to be wide enough to accommodate your widest title. Set the value of this property to an [`NSSet`](../../Foundation/nsset.md) object containing all the titles you intend as possible titles for the bar button item. Use the actual text strings you intend to display.

This property applies to bar button items placed on navigation bars or toolbars.

## See Also

### Customizing item appearance
- [var style: UIBarButtonItem.Style](./style-swift.property.md)
  The style of the item.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/possibletitles)*