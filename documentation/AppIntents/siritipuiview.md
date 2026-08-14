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
- [UIView](../uikit/uiview.md)
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
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [struct SiriTipView](siritipview.md)
  A SwiftUI view that displays the phrase someone uses to invoke an App Shortcut.
- [struct SiriTipViewStyle](siritipviewstyle.md)
  The styles to apply to the tip views you use to display spoken phrases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipuiview)*