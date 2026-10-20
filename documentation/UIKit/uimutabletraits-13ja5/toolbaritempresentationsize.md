# toolbarItemPresentationSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The presentation size of a toolbar item in an AppKit toolbar.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
var toolbarItemPresentationSize: UINSToolbarItemPresentationSize { get set }
```

#### Discussion

[`NSToolbar`](../../AppKit/nstoolbar.md) supports various display modes that affect the amount of space available for displaying toolbar items. If you use [`NSUIViewToolbarItem`](../nsuiviewtoolbaritem.md) to host a [`UIView`](../uiview.md) in an [`NSToolbar`](../../AppKit/nstoolbar.md) when you build your app with Mac Catalyst, that view receives information about its expected size through this trait. Use this trait to make any necessary adjustments to your custom view when the trait collection changes, such as when the toolbar switches to a new display mode.

The default value of this trait is [`UINSToolbarItemPresentationSize.unspecified`](../uinstoolbaritempresentationsize/unspecified.md) when an [`NSToolbar`](../../AppKit/nstoolbar.md) doesn’t host the view.

## See Also

### Getting and setting trait values
- [var accessibilityContrast: UIAccessibilityContrast](./accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [var activeAppearance: UIUserInterfaceActiveAppearance](./activeappearance.md)
  A property that indicates whether a scene has an active appearance.
- [var displayGamut: UIDisplayGamut](./displaygamut.md)
  The gamut of the current display.
- [var displayScale: CGFloat](./displayscale.md)
  The display scale of the trait collection.
- [var forceTouchCapability: UIForceTouchCapability](./forcetouchcapability.md)
  The Force Touch capability value of the trait collection.
- [var headroomUsageLimit: UITraitHDRHeadroomUsageLimit.Value](./headroomusagelimit.md)
  The HDR headroom usage limit associated with the current environment.
- [var horizontalSizeClass: UIUserInterfaceSizeClass](./horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [var imageDynamicRange: UIImage.DynamicRange](./imagedynamicrange.md)
  The image dynamic range associated with the current environment.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](./layoutdirection.md)
  The layout direction associated with the current environment.
- [var legibilityWeight: UILegibilityWeight](./legibilityweight.md)
  The font weight to apply to text.
- [var listEnvironment: UIListEnvironment](./listenvironment.md)
  The style of the containing list in a collection view or table view.
- [var preferredContentSizeCategory: UIContentSizeCategory](./preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [var resolvesNaturalAlignmentWithBaseWritingDirection: Bool](./resolvesnaturalalignmentwithbasewritingdirection.md)
  The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [var sceneCaptureState: UISceneCaptureState](./scenecapturestate.md)
  The scene capture state for the current environment.
- [var splitViewControllerLayoutEnvironment: UISplitViewController.LayoutEnvironment](./splitviewcontrollerlayoutenvironment.md)
  The split view controller layout for the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/toolbaritempresentationsize)*