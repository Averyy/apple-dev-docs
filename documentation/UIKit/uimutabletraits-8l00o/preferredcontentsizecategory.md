# preferredContentSizeCategory

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The font sizing option preferred by the user.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy) UIContentSizeCategory preferredContentSizeCategory;
```

## Discussion

With Dynamic Type, users can ask that apps display text using fonts that are larger or smaller than the normal font size defined by the system. For example, a user with a visual impairment might request a larger default font size to make it easier to read text. Use the value of this property to request a [`UIFont`](../uifont.md) object that matches the user’s requested size.

## See Also

### Getting and setting trait values
- [accessibilityContrast](./accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [activeAppearance](./activeappearance.md)
  A property that indicates whether a scene has an active appearance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-8l00o/preferredcontentsizecategory)*