# SWAttributionView

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

A view that displays the sender who shares a highlight and provides related actions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class SWAttributionView
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface SWAttributionView : UIView
```

*macOS*

```objc
@interface SWAttributionView : NSView
```

## Mentions

- [Making your app content shareable](./making-your-app-content-shareable.md)

#### Overview

The `SWAttributionView` also allows users to get back to the conversation about the [`SWHighlight`](./swhighlight.md) content, and other related actions using a [`highlightMenu`](./swattributionview/highlightmenu.md).

Place an `SWAttributionView` next to the content represented by its `SWHighlight`. The `SWAttributionView` displays the names and avatars within the provided horizontal space.

You can constrain this view’s width anchor or set its frame width to control the maximum width of its contents after which truncation may occur. Don’t constrain the view’s height, as the height is dependent on the [`preferredContentSizeCategory`](../UIKit/uiapplication/preferredcontentsizecategory.md), and the resulting font size. To provide enough vertical space around this view, reference its [`heightAnchor`](../UIKit/uiview/heightanchor.md) when using Auto Layout, or its [`intrinsicContentSize`](../UIKit/uiview/intrinsiccontentsize.md) when using manual layout.

## Topics

### Customizing highlights
- [var backgroundStyle: SWAttributionView.BackgroundStyle](./swattributionview/backgroundstyle-swift.property.md)
  The background style of the child view that contains names and avatars.
- [var displayContext: SWAttributionView.DisplayContext](./swattributionview/displaycontext-swift.property.md)
  The context for the content the system displays with this view.
- [var highlight: SWHighlight?](./swattributionview/highlight.md)
  The highlight you use to display this attribution.
- [var highlightMenu: UIMenu](./swattributionview/highlightmenu.md)
  A menu with a list of system actions specific to this hightlight.
- [var horizontalAlignment: SWAttributionView.HorizontalAlignment](./swattributionview/horizontalalignment-swift.property.md)
  The horizontal alignment of the view.
- [var menuTitleForHideAction: String?](./swattributionview/menutitleforhideaction.md)
  A localized string the system uses as a custom title for the hide menu item.
- [var preferredMaxLayoutWidth: CGFloat](./swattributionview/preferredmaxlayoutwidth.md)
  A width the system uses to constrain the view contents.
- [var supplementalMenu: UIMenu?](./swattributionview/supplementalmenu.md)
  A supplemental menu to augment the attribution view’s existing menu.
- [enablesMarquee](./swattributionview/enablesmarquee.md)
  Automatically enables a marquee effect.
### Customizing the view
- [SWAttributionView.BackgroundStyle](./swattributionview/backgroundstyle-swift.enum.md)
  The background styling of the attribution view’s contents.
- [SWAttributionView.DisplayContext](./swattributionview/displaycontext-swift.enum.md)
  The context for the content that influences the ranking of this view’s highlight.
- [SWAttributionView.HorizontalAlignment](./swattributionview/horizontalalignment-swift.enum.md)
  The horizontal alignment of attribution view’s contents.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview)*