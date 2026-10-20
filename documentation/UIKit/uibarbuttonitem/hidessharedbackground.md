# hidesSharedBackground

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A boolean value indicating whether the background this item may share with other items in the bar should be hidden.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var hidesSharedBackground: Bool { get set }
```

```objc
@property (nonatomic) BOOL hidesSharedBackground;
```

#### Discussion

Set this property to `YES` to prevent the standard shared background (typically using the Glass effect) from being drawn behind this bar button item.

This item will not be visually grouped with any other items, without the standard shared background. This property is ignored if the item is in a `UIBarButtonItemGroup` with more than one item. The default value is `NO`.

## See Also

### Customizing placement in a toolbar
- [var sharesBackground: Bool](./sharesbackground.md)
  A boolean value indicating whether this bar button item can share a background with other items in a navigation bar or a toolbar.
- [var axisBehavior: UIBarButtonItem.AxisBehavior](./axisbehavior-swift.property.md)
  The bar axis behavior of the item.
- [UIBarButtonItem.AxisBehavior](./axisbehavior-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/hidessharedbackground)*