# UIMutableTraits

**Framework**: UIKit  
**Kind**: protocol

A mutable container of traits.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
protocol UIMutableTraits
```

#### Overview

The [`UIMutableTraits`](uimutabletraits-13ja5.md) protocol provides read-write access to get and set trait values on an underlying container. UIKit uses this protocol to facilitate working with instances of [`UITraitCollection`](uitraitcollection.md), which are immutable and read-only. The [`UITraitCollection`](uitraitcollection.md) initializer [`init(mutations:)`](uitraitcollection/init(mutations:).md) uses an instance of [`UIMutableTraits`](uimutabletraits-13ja5.md), which enables you to set a batch of trait values in one method call. [`UITraitOverrides`](uitraitoverrides-swift.struct.md) conforms to [`UIMutableTraits`](uimutabletraits-13ja5.md), making it easy to set trait overrides on trait environments such as views and view controllers.

When you define a custom trait, declare a property for the trait in an extension to [`UIMutableTraits`](uimutabletraits-13ja5.md) so that you can access your custom trait using standard property syntax.

The following example defines an extension and sets the theme on the [`traitOverrides`](uiview/traitoverrides-fd9z.md) property:

```swift
// ThemeTrait conforms to UITraitDefinition, and has a defaultValue type of Theme
extension UIMutableTraits {
    var theme: Theme {
        get { self[ThemeTrait.self] }
        set { self[ThemeTrait.self] = newValue }
    }
}

// Apply an override for the custom theme trait.
view.traitOverrides.theme = .monochrome
```

## Topics

### Defining custom traits
- [var accessibilityContrast: UIAccessibilityContrast](uimutabletraits-13ja5/accessibilitycontrast.md)
- [struct UITraitAccessibilityContrast](uitraitaccessibilitycontrast-swift.struct.md)
- [var activeAppearance: UIUserInterfaceActiveAppearance](uimutabletraits-13ja5/activeappearance.md)
- [struct UITraitActiveAppearance](uitraitactiveappearance-swift.struct.md)
- [var displayGamut: UIDisplayGamut](uimutabletraits-13ja5/displaygamut.md)
- [struct UITraitDisplayGamut](uitraitdisplaygamut-swift.struct.md)
- [var displayScale: CGFloat](uimutabletraits-13ja5/displayscale.md)
- [struct UITraitDisplayScale](uitraitdisplayscale-swift.struct.md)
- [var forceTouchCapability: UIForceTouchCapability](uimutabletraits-13ja5/forcetouchcapability.md)
- [struct UITraitForceTouchCapability](uitraitforcetouchcapability-swift.struct.md)
- [var horizontalSizeClass: UIUserInterfaceSizeClass](uimutabletraits-13ja5/horizontalsizeclass.md)
- [struct UITraitHorizontalSizeClass](uitraithorizontalsizeclass-swift.struct.md)
- [var imageDynamicRange: UIImage.DynamicRange](uimutabletraits-13ja5/imagedynamicrange.md)
- [struct UITraitImageDynamicRange](uitraitimagedynamicrange-swift.struct.md)
- [var layoutDirection: UITraitEnvironmentLayoutDirection](uimutabletraits-13ja5/layoutdirection.md)
- [struct UITraitLayoutDirection](uitraitlayoutdirection-swift.struct.md)
- [var legibilityWeight: UILegibilityWeight](uimutabletraits-13ja5/legibilityweight.md)
- [struct UITraitLegibilityWeight](uitraitlegibilityweight-swift.struct.md)
- [var listEnvironment: UIListEnvironment](uimutabletraits-13ja5/listenvironment.md)
- [struct UITraitListEnvironment](uitraitlistenvironment-swift.struct.md)
- [var preferredContentSizeCategory: UIContentSizeCategory](uimutabletraits-13ja5/preferredcontentsizecategory.md)
- [struct UITraitPreferredContentSizeCategory](uitraitpreferredcontentsizecategory-swift.struct.md)
- [var sceneCaptureState: UISceneCaptureState](uimutabletraits-13ja5/scenecapturestate.md)
- [struct UITraitSceneCaptureState](uitraitscenecapturestate-swift.struct.md)
- [var toolbarItemPresentationSize: UINSToolbarItemPresentationSize](uimutabletraits-13ja5/toolbaritempresentationsize.md)
- [struct UITraitToolbarItemPresentationSize](uitraittoolbaritempresentationsize-swift.struct.md)
- [var typesettingLanguage: Locale.Language?](uimutabletraits-13ja5/typesettinglanguage.md)
- [struct UITraitTypesettingLanguage](uitraittypesettinglanguage-swift.struct.md)
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uimutabletraits-13ja5/userinterfaceidiom.md)
- [struct UITraitUserInterfaceIdiom](uitraituserinterfaceidiom-swift.struct.md)
- [var userInterfaceLevel: UIUserInterfaceLevel](uimutabletraits-13ja5/userinterfacelevel.md)
- [struct UITraitUserInterfaceLevel](uitraituserinterfacelevel-swift.struct.md)
- [var userInterfaceStyle: UIUserInterfaceStyle](uimutabletraits-13ja5/userinterfacestyle.md)
- [struct UITraitUserInterfaceStyle](uitraituserinterfacestyle-swift.struct.md)
- [var verticalSizeClass: UIUserInterfaceSizeClass](uimutabletraits-13ja5/verticalsizeclass.md)
- [struct UITraitVerticalSizeClass](uitraitverticalsizeclass-swift.struct.md)
### Subscripts
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-19j2e.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-1b2k9.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-1k64j.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-2n1bn.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-2tbov.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-4tqsr.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-5h7go.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-6s6f5.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-7jap6.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-7kxs.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-7m9p0.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-8vqxe.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-9ld0y.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-9za2c.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-dwij.md)
- [subscript<T>(T.Type) -> T.Value](uimutabletraits-13ja5/subscript(_:)-ve6h.md)

## Relationships

### Conforming Types
- [UITraitOverrides](uitraitoverrides-swift.struct.md)

## See Also

- [convenience init(mutations: (inout any UIMutableTraits) -> Void)](uitraitcollection/init(mutations:).md)
- [func modifyingTraits((inout any UIMutableTraits) -> Void) -> UITraitCollection](uitraitcollection/modifyingtraits(_:).md)
- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [Responding to changing display modes on Apple TV](responding-to-changing-display-modes-on-apple-tv.md)
  Change images and resources dynamically when the screen gamut on your device changes.
- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5)*