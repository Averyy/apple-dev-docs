# LPLinkView

**Framework**: Link Presentation  
**Kind**: class  
**Role**: Class

A rich visual representation of a link.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class LPLinkView
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@interface LPLinkView : UIView
```

*macOS*

```objc
@interface LPLinkView : NSView
```

## Overview

[`LPLinkView`](./lplinkview.md) presents a link based on its available metadata. Use it to show a link’s title and icon, associated images, inline audio, video playback, and maps in a familiar and consistent style.

## Present a rich link

To present a rich link in your app, create an [`LPLinkView`](./lplinkview.md), passing an [`LPLinkMetadata`](./lplinkmetadata.md) instance into its initializer. Then add the [`LPLinkView`](./lplinkview.md) to your view.

For example, to present links in a table view, add an [`LPLinkView`](./lplinkview.md) instance as a subview when populating each cell.

```swift
let linkView = LPLinkView(metadata: metadata)
cell.contentView.addSubview(linkView)
linkView.sizeToFit()
```

[`LPLinkView`](./lplinkview.md) has an intrinsic size, but it also responds to [`sizeToFit()`](../UIKit/uiview/sizetofit%28%29.md) to present a layout at any size.

## Topics

### Creating a link view
- [init(metadata: LPLinkMetadata)](./lplinkview/init%28metadata%29.md)
  Initializes a link view with specified metadata.
- [init(url: URL)](./lplinkview/init%28url%29-6f6kt.md)
  Initializes a placeholder link view without metadata for a given URL.
### Specifying metadata
- [var metadata: LPLinkMetadata](./lplinkview/metadata.md)
  The metadata from which to generate a rich presentation.
### Initializers
- [init(URL: URL)](./lplinkview/init%28url%29-8r0tp.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkview)*