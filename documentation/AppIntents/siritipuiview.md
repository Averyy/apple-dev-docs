# SiriTipUIView

**Framework**: App Intents  
**Kind**: class  
**Role**: Class

A view that displays the phrase a person uses to invoke an App Shortcut.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS

## Declaration

```swift
@MainActor
@objc @preconcurrency final class SiriTipUIView
```

#### Overview

You must call [`setIntent(intent:)`](./siritipuiview/setintent%28intent%29.md) before displaying the view.

## Topics

### Creating a tip view
- [init(style: SiriTipViewStyle)](./siritipuiview/init%28style%29.md)
  A view that displays the phrase for an App Shortcut.
### Getting the view style
- [var style: SiriTipViewStyle](./siritipuiview/style.md)
  The style to use for the view.
- [struct SiriTipViewStyle](./siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.
### Getting the view’s configuration
- [var allowsDismissal: Bool](./siritipuiview/allowsdismissal.md)
  Indicates if the tip view should display a dismissal button
- [var isPresented: Bool](./siritipuiview/ispresented.md)
  Determines if the view should be presented to the user.
### Instance Properties
- [var intrinsicContentSize: CGSize](./siritipuiview/intrinsiccontentsize.md)
### Instance Methods
- [func didMoveToWindow()](./siritipuiview/didmovetowindow%28%29.md)
- [func setIntent<Intent>(intent: Intent)](./siritipuiview/setintent%28intent%29.md)
  Sets an `AppIntent` for this view. This must be called before presenting the view.
- [func sizeThatFits(CGSize) -> CGSize](./siritipuiview/sizethatfits%28_%29.md)

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
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
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Tip views
- [struct SiriTipView](./siritipview.md)
  A SwiftUI view that displays the phrase someone uses to invoke an App Shortcut.
- [struct SiriTipViewStyle](./siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipuiview)*