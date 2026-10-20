# ShortcutsUIButton

**Framework**: App Intents  
**Kind**: class  
**Role**: Class

A button that opens the current app’s page in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@objc @preconcurrency final class ShortcutsUIButton
```

#### Overview

You can add additional targets to observe when the button is tapped.

## Topics

### Creating the button
- [init(style: ShortcutsLinkStyle)](./shortcutsuibutton/init%28style%29.md)
  Creates a button with the specified style.
### Getting the button style
- [var style: ShortcutsLinkStyle](./shortcutsuibutton/style.md)
  The style to use for the button.
### Configuring additional actions
- [func addTarget(Any?, action: Selector, for: UIControl.Event)](./shortcutsuibutton/addtarget%28_,action,for%29.md)
### Resizing the button
- [func sizeThatFits(CGSize) -> CGSize](./shortcutsuibutton/sizethatfits%28_%29.md)

## Relationships

### Inherits From
- [UIButton](../UIKit/uibutton.md)
### Conforms To
- [AppEntityAnnotatable](./appentityannotatable.md)
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../UIKit/uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](../UIKit/uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Buttons
- [struct ShortcutsLink](./shortcutslink.md)
  A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.
- [struct ShortcutsLinkStyle](./shortcutslinkstyle.md)
  The styles to apply to buttons you use to open your app’s page in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutsuibutton)*