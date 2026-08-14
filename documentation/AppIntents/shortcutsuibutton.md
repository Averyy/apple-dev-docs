# ShortcutsUIButton

**Framework**: App Intents  
**Kind**: class

A button that opens the current app’s page in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class ShortcutsUIButton
```

#### Overview

You can add additional targets to observe when the button is tapped.

## Topics

### Creating the button
- [init(style: ShortcutsLinkStyle)](shortcutsuibutton/init(style:).md)
  Creates a button with the specified style.
### Getting the button style
- [var style: ShortcutsLinkStyle](shortcutsuibutton/style.md)
  The style to use for the button.
### Configuring additional actions
- [func addTarget(Any?, action: Selector, for: UIControl.Event)](shortcutsuibutton/addtarget(_:action:for:).md)
### Resizing the button
- [func sizeThatFits(CGSize) -> CGSize](shortcutsuibutton/sizethatfits(_:).md)

## Relationships

### Inherits From
- [UIButton](../uikit/uibutton.md)
### Conforms To
- [AppEntityAnnotatable](appentityannotatable.md)
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../uikit/uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../uikit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](../uikit/uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [struct ShortcutsLink](shortcutslink.md)
  A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.
- [struct ShortcutsLinkStyle](shortcutslinkstyle.md)
  The styles to apply to buttons you use to open your app’s page in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutsuibutton)*