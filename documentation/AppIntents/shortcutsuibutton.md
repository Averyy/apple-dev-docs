# ShortcutsUIButton

**Framework**: App Intents  
**Kind**: class

A button that opens the current app’s page in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

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
- [UIButton](../UIKit/UIButton.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../UIKit/UIAccessibilityContentSizeCategoryImageAdjusting.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/UIContextMenuInteractionDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UISpringLoadedInteractionSupporting](../UIKit/UISpringLoadedInteractionSupporting.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [struct ShortcutsLink](shortcutslink.md)
  A button that brings users to the current app’s App Shortcuts page in the Shortcuts app.
- [struct ShortcutsLinkStyle](shortcutslinkstyle.md)
  The styles to apply to buttons you use to open your app’s page in the Shortcuts app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutsuibutton)*