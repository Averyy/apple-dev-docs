# PDFView

**Framework**: PDFKit  
**Kind**: class

An object that encapsulates the functionality of PDF Kit into a single widget that you can add to your application using Interface Builder.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PDFView
```

## Mentions

- [Adding Custom Graphics to a PDF](adding-custom-graphics-to-a-pdf.md)

#### Overview

`PDFView` may be the only class you need to deal with for adding PDF functionality to your application. It lets you display PDF data and allows users to select content, navigate through a document, set zoom level, and copy textual content to the Pasteboard. `PDFView` also keeps track of page history.

You can subclass `PDFView` to create a custom PDF viewer.

You can also create a custom PDF viewer by using the PDF Kit utility classes directly and not using `PDFView` at all.

## Topics

### Associating a Document with a View
- [var document: PDFDocument?](pdfview/document.md)
  Returns the document associated with a `PDFView` object.
- [func takePasswordFrom(Any)](pdfview/takepasswordfrom(_:).md)
  Unlocks with the password from the specified sender.
### Configuring Document View
- [Configurations](configurations.md)
  Define display modes, scaling, rendering, printing and graphics properties.
### Interacting in a View
- [Document Interactions](document-interactions.md)
  Handle selections, work with annotation actions, convert page and view points, and work with mouse events in a document.
### Navigating Within a Document
- [var currentPage: PDFPage?](pdfview/currentpage.md)
  Returns the current page.
- [var currentDestination: PDFDestination?](pdfview/currentdestination.md)
  Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.
- [var visiblePages: [PDFPage]](pdfview/visiblepages.md)
  Returns an array of `PDFPage` objects that represent the currently visible pages.
- [Navigation](navigation.md)
  Operations for moving through page history and seeking to a page in a document.
### Setting the Delegate
- [var delegate: (any PDFViewDelegate)?](pdfview/delegate.md)
  Returns the view’s delegate.
- [protocol PDFViewDelegate](pdfviewdelegate.md)
  The delegate for the `PDFView` object.
### Instance Properties
- [var findInteraction: UIFindInteraction](pdfview/findinteraction.md)
- [var isFindInteractionEnabled: Bool](pdfview/isfindinteractionenabled.md)
- [var isInMarkupMode: Bool](pdfview/isinmarkupmode.md)
- [var pageOverlayViewProvider: (any PDFPageOverlayViewProvider)?](pdfview/pageoverlayviewprovider.md)
- [var pageShadowsEnabled: Bool](pdfview/pageshadowsenabled.md)

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
- [NSAnimationDelegate](../appkit/nsanimationdelegate.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSMenuDelegate](../appkit/nsmenudelegate.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFindInteractionDelegate](../uikit/uifindinteractiondelegate.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UIGestureRecognizerDelegate](../uikit/uigesturerecognizerdelegate.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class PDFThumbnailView](pdfthumbnailview.md)
  An object that contains a set of thumbnails, each of which represents a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview)*