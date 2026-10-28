# prefersLargeTitles

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the title displays in a large format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var prefersLargeTitles: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL prefersLargeTitles;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), the navigation bar allows the title to be displayed out-of-line and using a larger font. The navigation item used to build the bar must specify whether it wants its title displayed in the large or small format. Use the [`largeTitleDisplayMode`](../uinavigationitem/largetitledisplaymode-swift.property.md) property to configure the title’s appearance.

When the property is set to [`false`](../../Swift/false.md), the navigation bar displays the title inline with the other bar button items.

## See Also

### Customizing the bar’s appearance
- [var standardAppearance: UINavigationBarAppearance](./standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](./compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](./scrolledgeappearance.md)
  The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](./compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var isTranslucent: Bool](./istranslucent.md)
  A Boolean value that indicates whether the navigation bar is translucent.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md)
  Customize appearance information directly on the navigation bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/preferslargetitles)*