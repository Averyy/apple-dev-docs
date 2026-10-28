# isTranslucent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the navigation bar is translucent.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isTranslucent: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isTranslucent) BOOL translucent;
```

## Discussion

When the navigation bar is translucent, configure the [`edgesForExtendedLayout`](../uiviewcontroller/edgesforextendedlayout.md) and [`extendedLayoutIncludesOpaqueBars`](../uiviewcontroller/extendedlayoutincludesopaquebars.md) properties of your view controller to display your content underneath the navigation bar.

If the navigation bar doesn’t have a custom background image, or if any pixel of the background image has an alpha value of less than `1.0`, the default value of this property is [`true`](../../Swift/true.md). If the background image is completely opaque, the default value of this property is [`false`](../../Swift/false.md). If you set this property to [`true`](../../Swift/true.md) and the custom background image is completely opaque, UIKit applies a system-defined opacity of less than `1.0` to the image. If you set this property to [`false`](../../Swift/false.md) and the background image is not opaque, UIKit adds an opaque backdrop.

## See Also

### Customizing the bar’s appearance
- [var prefersLargeTitles: Bool](./preferslargetitles.md)
  A Boolean value that indicates whether the title displays in a large format.
- [var standardAppearance: UINavigationBarAppearance](./standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](./compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](./scrolledgeappearance.md)
  The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](./compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [Legacy customizations](../uinavigationbar-legacy-customizations.md)
  Customize appearance information directly on the navigation bar object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/istranslucent)*