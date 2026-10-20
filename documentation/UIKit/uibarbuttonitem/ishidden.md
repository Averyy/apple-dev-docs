# isHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that determines the visibility of the item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isHidden) BOOL hidden;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to hide the item, or [`false`](../../Swift/false.md) to display the item.

## See Also

### Customizing item appearance
- [var style: UIBarButtonItem.Style](./style-swift.property.md)
  The style of the item.
- [UIBarButtonItem.Style](./style-swift.enum.md)
  Constants that specify the style of an item.
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the button item.
- [var isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the button is in a selected state.
- [var width: CGFloat](./width.md)
  The width of the item.
- [var possibleTitles: Set<String>?](./possibletitles.md)
  The set of possible titles to display on the bar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/ishidden)*