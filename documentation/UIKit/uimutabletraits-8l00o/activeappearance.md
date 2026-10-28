# activeAppearance

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A property that indicates whether a scene has an active appearance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) UIUserInterfaceActiveAppearance activeAppearance;
```

## Discussion

`activeAppearance` describes whether a scene is frontmost; it doesn’t describe a scene’s life-cycle state. A scene that isn’t frontmost can remain in the [`UIScene.ActivationState.foregroundActive`](../uiscene/activationstate-swift.enum/foregroundactive.md) activation state as long as it can still receive user interaction. Its activation state changes to [`UIScene.ActivationState.foregroundInactive`](../uiscene/activationstate-swift.enum/foregroundinactive.md) only when a system interruption takes over interaction. This can happen because of Control Center, an alert, Siri, App Switcher, or another app’s window covering it in windowed apps. Use [`UIScene.ActivationState`](../uiscene/activationstate-swift.enum.md) to decide when to save view state, and use `activeAppearance` to detect when a scene is no longer frontmost.

Because `activeAppearance` belongs to a scene’s trait collection, each scene has its own value, even in apps that support multiple scenes. To detect when a scene becomes frontmost, register for changes to this trait by calling [`registerForTraitChanges(_:handler:)`](../uitraitchangeobservable-67e94/registerfortraitchanges%28_,handler%29.md) on the window scene, or on any view or view controller in its hierarchy.

In Mac apps built with Mac Catalyst, Stage Manager on iPad, and a windowed app on iPad, the value is `.active` when the window is focused (the key window) and `.inactive` when it isn’t. A window that another app’s window covers keeps an `.active` appearance as long as it remains the focused window.

In iOS and in a full-screen app on iPad, the value reflects whether the app itself is in the foreground (`.active`) or not (`.inactive`).

## See Also

### Getting and setting trait values
- [accessibilityContrast](./accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [displayGamut](./displaygamut.md)
  The gamut of the current display.
- [displayScale](./displayscale.md)
  The display scale of the trait collection.
- [forceTouchCapability](./forcetouchcapability.md)
  The Force Touch capability value of the trait collection.
- [horizontalSizeClass](./horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [imageDynamicRange](./imagedynamicrange.md)
  The image dynamic range associated with the current environment.
- [layoutDirection](./layoutdirection.md)
  The layout direction associated with the current environment.
- [legibilityWeight](./legibilityweight.md)
  The font weight to apply to text.
- [listEnvironment](./listenvironment.md)
  The style of the containing list in a collection view or table view.
- [preferredContentSizeCategory](./preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [resolvesNaturalAlignmentWithBaseWritingDirection](./resolvesnaturalalignmentwithbasewritingdirection.md)
  The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [sceneCaptureState](./scenecapturestate.md)
  The scene capture state for the current environment.
- [splitViewControllerLayoutEnvironment](./splitviewcontrollerlayoutenvironment.md)
  The split view controller layout for the current environment.
- [tabAccessoryEnvironment](./tabaccessoryenvironment.md)
  The tab accessory environment for the current trait collection.
- [toolbarItemPresentationSize](./toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-8l00o/activeappearance)*