# UINSToolbarItemPresentationSize

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the presentation size of a toolbar item in an AppKit toolbar.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst 16.0+
- tvOS
- visionOS

## Declaration

```swift
enum UINSToolbarItemPresentationSize
```

```c
enum UINSToolbarItemPresentationSize : NSInteger;
```

## Overview

Use these constants with [`toolbarItemPresentationSize`](./uitraitcollection/toolbaritempresentationsize.md) to determine what size an [`NSToolbar`](../AppKit/nstoolbar.md) expects its toolbar items to be.

## Topics

### Constants
- [UINSToolbarItemPresentationSize.regular](./uinstoolbaritempresentationsize/regular.md)
  The default, regular presentation size.
- [UINSToolbarItemPresentationSize.small](./uinstoolbaritempresentationsize/small.md)
  The smallest presentation size.
- [UINSToolbarItemPresentationSize.large](./uinstoolbaritempresentationsize/large.md)
  The largest presentation size.
- [UINSToolbarItemPresentationSize.unspecified](./uinstoolbaritempresentationsize/unspecified.md)
  An unspecified presentation size.
### Initializers
- [init?(rawValue: Int)](./uinstoolbaritempresentationsize/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Retrieving interface-related traits
- [var userInterfaceStyle: UIUserInterfaceStyle](./uitraitcollection/userinterfacestyle.md)
  The style associated with the user interface.
- [enum UIUserInterfaceStyle](./uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](./uitraitcollection/userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [enum UIUserInterfaceIdiom](./uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [var userInterfaceLevel: UIUserInterfaceLevel](./uitraitcollection/userinterfacelevel.md)
  The elevation level of the interface.
- [enum UIUserInterfaceLevel](./uiuserinterfacelevel.md)
  Constants that indicate the visual level for content in the window.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](./uitraitcollection/layoutdirection.md)
  The layout direction associated with the current environment.
- [enum UITraitEnvironmentLayoutDirection](./uitraitenvironmentlayoutdirection.md)
  Constants that indicate the layout direction associated with the current environment.
- [var resolvesNaturalAlignmentWithBaseWritingDirection: Bool](./uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [var accessibilityContrast: UIAccessibilityContrast](./uitraitcollection/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [enum UIAccessibilityContrast](./uiaccessibilitycontrast.md)
  Constants that indicate the accessibility contrast setting.
- [var legibilityWeight: UILegibilityWeight](./uitraitcollection/legibilityweight.md)
  The font weight to apply to text.
- [enum UILegibilityWeight](./uilegibilityweight.md)
  Constants that indicate the weight to apply to text in your interface.
- [var activeAppearance: UIUserInterfaceActiveAppearance](./uitraitcollection/activeappearance.md)
  A property that indicates whether a scene has an active appearance.
- [enum UIUserInterfaceActiveAppearance](./uiuserinterfaceactiveappearance.md)
  Constants that indicate whether the user interface has an active appearance.
- [resolvesNaturalAlignmentWithBaseWritingDirection](./uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy.md)
  Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinstoolbaritempresentationsize)*