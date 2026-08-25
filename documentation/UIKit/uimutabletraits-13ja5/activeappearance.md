# activeAppearance

**Framework**: UIKit  
**Kind**: property

A property that indicates whether a scene has an active appearance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
var activeAppearance: UIUserInterfaceActiveAppearance { get set }
```

#### Discussion

`activeAppearance` describes whether a scene is frontmost; it doesn’t describe a scene’s life-cycle state. A scene that isn’t frontmost can remain in the [`UIScene.ActivationState.foregroundActive`](uiscene/activationstate-swift.enum/foregroundactive.md) activation state as long as it can still receive user interaction. Its activation state changes to [`UIScene.ActivationState.foregroundInactive`](uiscene/activationstate-swift.enum/foregroundinactive.md) only when a system interruption takes over interaction. This can happen because of Control Center, an alert, Siri, App Switcher, or another app’s window covering it in windowed apps. Use [`UIScene.ActivationState`](uiscene/activationstate-swift.enum.md) to decide when to save view state, and use `activeAppearance` to detect when a scene is no longer frontmost.

Because `activeAppearance` belongs to a scene’s trait collection, each scene has its own value, even in apps that support multiple scenes. To detect when a scene becomes frontmost, register for changes to this trait by calling [`registerForTraitChanges(_:handler:)`](uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:).md) on the window scene, or on any view or view controller in its hierarchy.

In Mac apps built with Mac Catalyst, Stage Manager on iPad, and a windowed app on iPad, the value is `.active` when the window is focused (the key window) and `.inactive` when it isn’t. A window that another app’s window covers keeps an `.active` appearance as long as it remains the focused window.

In iOS and in a full-screen app on iPad, the value reflects whether the app itself is in the foreground (`.active`) or not (`.inactive`).

## See Also

- [var accessibilityContrast: UIAccessibilityContrast](uimutabletraits-13ja5/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
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
- [var tabAccessoryEnvironment: UITabAccessory.Environment](uimutabletraits-13ja5/tabaccessoryenvironment.md)
  The tab accessory environment for the current trait collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/activeappearance)*