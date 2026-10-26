# UIAccessibilityContrast

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the accessibility contrast setting.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum UIAccessibilityContrast
```

```c
enum UIAccessibilityContrast : NSInteger;
```

## Topics

### Contrast settings
- [UIAccessibilityContrast.unspecified](./uiaccessibilitycontrast/unspecified.md)
  An unspecified contrast.
- [UIAccessibilityContrast.normal](./uiaccessibilitycontrast/normal.md)
  A normal contrast level.
- [UIAccessibilityContrast.high](./uiaccessibilitycontrast/high.md)
  A high contrast level.
### Initializers
- [init(ColorSchemeContrast?)](./uiaccessibilitycontrast/init%28_%29.md)
  Creates an accessibility contrast from the specified SwiftUI color scheme contrast.
- [init?(rawValue: Int)](./uiaccessibilitycontrast/init%28rawvalue%29.md)

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
- [var legibilityWeight: UILegibilityWeight](./uitraitcollection/legibilityweight.md)
  The font weight to apply to text.
- [enum UILegibilityWeight](./uilegibilityweight.md)
  Constants that indicate the weight to apply to text in your interface.
- [var activeAppearance: UIUserInterfaceActiveAppearance](./uitraitcollection/activeappearance.md)
  A property that indicates whether a scene has an active appearance.
- [enum UIUserInterfaceActiveAppearance](./uiuserinterfaceactiveappearance.md)
  Constants that indicate whether the user interface has an active appearance.
- [var toolbarItemPresentationSize: UINSToolbarItemPresentationSize](./uitraitcollection/toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.
- [resolvesNaturalAlignmentWithBaseWritingDirection](./uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy.md)
  Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitycontrast)*