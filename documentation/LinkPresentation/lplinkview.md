# LPLinkView

**Framework**: Link Presentation  
**Kind**: class

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

#### Overview

[`LPLinkView`](lplinkview.md) presents a link based on its available metadata. Use it to show a link’s title and icon, associated images, inline audio, video playback, and maps in a familiar and consistent style.

#### Present a Rich Link

To present a rich link in your app, create an [`LPLinkView`](lplinkview.md), passing an [`LPLinkMetadata`](lplinkmetadata.md) instance into its initializer. Then add the [`LPLinkView`](lplinkview.md) to your view.

For example, to present links in a table view, add an [`LPLinkView`](lplinkview.md) instance as a subview when populating each cell.

```swift
let linkView = LPLinkView(metadata: metadata)
cell.contentView.addSubview(linkView)
linkView.sizeToFit()
```

[`LPLinkView`](lplinkview.md) has an intrinsic size, but it also responds to [`sizeToFit()`](https://developer.apple.com/documentation/uikit/uiview/sizetofit()) to present a layout at any size.

## Topics

### Creating a link view
- [init(metadata: LPLinkMetadata)](lplinkview/init(metadata:).md)
  Initializes a link view with specified metadata.
- [init(url: URL)](lplinkview/init(url:)-6f6kt.md)
  Initializes a placeholder link view without metadata for a given URL.
### Specifying metadata
- [var metadata: LPLinkMetadata](lplinkview/metadata.md)
  The metadata from which to generate a rich presentation.
### Initializers
- [init(URL: URL)](lplinkview/init(url:)-8r0tp.md)

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkview)*