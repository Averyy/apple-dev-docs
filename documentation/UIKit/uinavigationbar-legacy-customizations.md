# Legacy customizations

**Framework**: UIKit  
**Role**: API Collection

Customize appearance information directly on the navigation bar object.

#### Overview

In iOS 13 and later, customize your navigation bar using the [`standardAppearance`](./uinavigationbar/standardappearance.md), [`compactAppearance`](./uinavigationbar/compactappearance.md), and [`scrollEdgeAppearance`](./uinavigationbar/scrolledgeappearance.md) properties. You may continue to use these legacy accessors to customize your navigation bar’s appearance directly, but you must update the appearance for different bar configurations yourself.

## Topics

### Configuring the navigation bar
- [Customizing your app’s navigation bar](./customizing-your-app-s-navigation-bar.md)
  Create custom titles, prompts, and buttons in your app’s navigation bar.
### Setting the bar’s style
- [var barStyle: UIBarStyle](./uinavigationbar/barstyle.md)
  The navigation bar style that specifies its appearance.
- [enum UIBarStyle](./uibarstyle.md)
  Defines the stylistic appearance of different types of views.
### Configuring the title
- [var titleTextAttributes: [NSAttributedString.Key : Any]?](./uinavigationbar/titletextattributes.md)
  Display attributes for the bar’s title text.
- [var largeTitleTextAttributes: [NSAttributedString.Key : Any]?](./uinavigationbar/largetitletextattributes.md)
  Display attributes for the bar’s large title text.
- [func titleVerticalPositionAdjustment(for: UIBarMetrics) -> CGFloat](./uinavigationbar/titleverticalpositionadjustment%28for%29.md)
  Returns the title’s vertical position adjustment for given bar metrics.
- [func setTitleVerticalPositionAdjustment(CGFloat, for: UIBarMetrics)](./uinavigationbar/settitleverticalpositionadjustment%28_,for%29.md)
  Sets the title’s vertical position adjustment for given bar metrics.
### Configuring bar button items
- [var tintColor: UIColor!](./uinavigationbar/tintcolor.md)
  The tint color to apply to the navigation items and bar button items.
### Configuring the Back button
- [var backIndicatorImage: UIImage?](./uinavigationbar/backindicatorimage.md)
  The image shown beside the Back button.
- [var backIndicatorTransitionMaskImage: UIImage?](./uinavigationbar/backindicatortransitionmaskimage.md)
  The image used as a mask for content during push and pop transitions.
### Changing the background
- [var barTintColor: UIColor?](./uinavigationbar/bartintcolor.md)
  The tint color to apply to the navigation bar background.
- [func backgroundImage(for: UIBarMetrics) -> UIImage?](./uinavigationbar/backgroundimage%28for%29.md)
  Returns the background image for given bar metrics.
- [func setBackgroundImage(UIImage?, for: UIBarMetrics)](./uinavigationbar/setbackgroundimage%28_,for%29.md)
  Sets the background image for given bar metrics.
- [func backgroundImage(for: UIBarPosition, barMetrics: UIBarMetrics) -> UIImage?](./uinavigationbar/backgroundimage%28for,barmetrics%29.md)
  Returns the background image to use for a given bar position and set of metrics.
- [func setBackgroundImage(UIImage?, for: UIBarPosition, barMetrics: UIBarMetrics)](./uinavigationbar/setbackgroundimage%28_,for,barmetrics%29.md)
  Sets the background image to use for a given bar position and set of metrics.
### Adding a shadow
- [var shadowImage: UIImage?](./uinavigationbar/shadowimage.md)
  The shadow image to be used for the navigation bar.

## See Also

### Customizing the bar’s appearance
- [var prefersLargeTitles: Bool](./uinavigationbar/preferslargetitles.md)
  A Boolean value that indicates whether the title displays in a large format.
- [var standardAppearance: UINavigationBarAppearance](./uinavigationbar/standardappearance.md)
  The appearance settings for a standard-height navigation bar.
- [var compactAppearance: UINavigationBarAppearance?](./uinavigationbar/compactappearance.md)
  The appearance settings for a compact-height navigation bar.
- [var scrollEdgeAppearance: UINavigationBarAppearance?](./uinavigationbar/scrolledgeappearance.md)
  The appearance settings for the navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var compactScrollEdgeAppearance: UINavigationBarAppearance?](./uinavigationbar/compactscrolledgeappearance.md)
  The appearance settings for a compact-height navigation bar when the edge of scrollable content aligns with the edge of the navigation bar.
- [var isTranslucent: Bool](./uinavigationbar/istranslucent.md)
  A Boolean value that indicates whether the navigation bar is translucent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar-legacy-customizations)*