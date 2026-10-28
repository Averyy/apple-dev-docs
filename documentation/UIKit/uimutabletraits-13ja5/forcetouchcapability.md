# forceTouchCapability

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The Force Touch capability value of the trait collection.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
var forceTouchCapability: UIForceTouchCapability { get set }
```

## Discussion

3D Touch is available only on certain devices. On those devices, availability is determined by the user’s associated accessibility setting in the Settings app. Check this property’s value on app launch, and in your implementation of the [`traitCollectionDidChange(_:)`](../uitraitenvironment/traitcollectiondidchange%28_%29.md) method.

If this property does not contain a value, the meaning is equivalent to the value [`UIForceTouchCapability.unknown`](../uiforcetouchcapability/unknown.md).

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
- [var tabAccessoryEnvironment: UITabAccessory.Environment](./tabaccessoryenvironment.md)
  The tab accessory environment for the current trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/forcetouchcapability)*