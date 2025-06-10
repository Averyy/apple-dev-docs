# SiriTipUIView

**Framework**: App Intents  
**Kind**: class

A view that displays the phrase a person uses to invoke an App Shortcut.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class SiriTipUIView
```

#### Overview

You must call `UISiriTip/setIntent(intent:)` before displaying the view.

## Topics

### Creating a tip view
- [init(style: SiriTipViewStyle)](siritipuiview/init(style:).md)
  A view that displays the phrase for an App Shortcut.
### Getting the view style
- [var style: SiriTipViewStyle](siritipuiview/style.md)
  The style to use for the view.
- [struct SiriTipViewStyle](siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.
### Getting the view’s configuration
- [var allowsDismissal: Bool](siritipuiview/allowsdismissal.md)
  Indicates if the tip view should display a dismissal button
- [var isPresented: Bool](siritipuiview/ispresented.md)
  Determines if the view should be presented to the user.
### Instance Properties
- [var intrinsicContentSize: CGSize](siritipuiview/intrinsiccontentsize.md)
### Instance Methods
- [func didMoveToWindow()](siritipuiview/didmovetowindow.md)
- [func setIntent<Intent>(intent: Intent)](siritipuiview/setintent(intent:).md)
  Sets an `AppIntent` for this view. This must be called before presenting the view.
- [func sizeThatFits(CGSize) -> CGSize](siritipuiview/sizethatfits(_:).md)

## Relationships

### Inherits From
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [struct SiriTipView](siritipview.md)
  A SwiftUI view that displays the phrase someone uses to invoke an App Shortcut.
- [struct SiriTipViewStyle](siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipuiview)*