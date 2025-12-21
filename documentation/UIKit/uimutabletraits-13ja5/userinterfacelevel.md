# userInterfaceLevel

**Framework**: UIKit  
**Kind**: property

The elevation level of the interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var userInterfaceLevel: UIUserInterfaceLevel { get set }
```

#### Discussion

Levels create a visual separation between different parts of your UI. Window content typically appears at the [`UIUserInterfaceLevel.base`](uiuserinterfacelevel/base.md) level. When you want parts of your UI to stand out from the underlying background, assign the [`UIUserInterfaceLevel.elevated`](uiuserinterfacelevel/elevated.md) level to them. For example, the system assigns the [`UIUserInterfaceLevel.elevated`](uiuserinterfacelevel/elevated.md) level to alerts and popovers.

## See Also

- [var accessibilityContrast: UIAccessibilityContrast](uimutabletraits-13ja5/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [var activeAppearance: UIUserInterfaceActiveAppearance](uimutabletraits-13ja5/activeappearance.md)
  A property that indicates whether the user interface has an active appearance.
- [var displayGamut: UIDisplayGamut](uimutabletraits-13ja5/displaygamut.md)
  The gamut of the current display.
- [var displayScale: CGFloat](uimutabletraits-13ja5/displayscale.md)
  The display scale of the trait collection.
- [var forceTouchCapability: UIForceTouchCapability](uimutabletraits-13ja5/forcetouchcapability.md)
  The Force Touch capability value of the trait collection.
- [var headroomUsageLimit: UITraitHDRHeadroomUsageLimit.Value](uimutabletraits-13ja5/headroomusagelimit.md)
  The HDR headroom usage limit associated with the current environment.
- [var horizontalSizeClass: UIUserInterfaceSizeClass](uimutabletraits-13ja5/horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [var imageDynamicRange: UIImage.DynamicRange](uimutabletraits-13ja5/imagedynamicrange.md)
  The image dynamic range associated with the current environment.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](uimutabletraits-13ja5/layoutdirection.md)
  The layout direction associated with the current environment.
- [var legibilityWeight: UILegibilityWeight](uimutabletraits-13ja5/legibilityweight.md)
  The font weight to apply to text.
- [var listEnvironment: UIListEnvironment](uimutabletraits-13ja5/listenvironment.md)
  The style of the containing list in a collection view or table view.
- [var preferredContentSizeCategory: UIContentSizeCategory](uimutabletraits-13ja5/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [var resolvesNaturalAlignmentWithBaseWritingDirection: Bool](uimutabletraits-13ja5/resolvesnaturalalignmentwithbasewritingdirection.md)
  The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [var sceneCaptureState: UISceneCaptureState](uimutabletraits-13ja5/scenecapturestate.md)
  The scene capture state for the current environment.
- [var splitViewControllerLayoutEnvironment: UISplitViewController.LayoutEnvironment](uimutabletraits-13ja5/splitviewcontrollerlayoutenvironment.md)
  The split view controller layout for the current environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/userinterfacelevel)*