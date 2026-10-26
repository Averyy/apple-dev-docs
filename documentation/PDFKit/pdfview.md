# PDFView

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface PDFView : UIView
```

*macOS*

```objc
@interface PDFView : NSView
```

## Mentions

- [Adding Custom Graphics to a PDF](./adding-custom-graphics-to-a-pdf.md)

#### Overview

`PDFView` may be the only class you need to deal with for adding PDF functionality to your application. It lets you display PDF data and allows users to select content, navigate through a document, set zoom level, and copy textual content to the Pasteboard. `PDFView` also keeps track of page history.

You can subclass `PDFView` to create a custom PDF viewer.

You can also create a custom PDF viewer by using the PDF Kit utility classes directly and not using `PDFView` at all.

## Topics

### Associating a Document with a View
- [var document: PDFDocument?](./pdfview/document.md)
  Returns the document associated with a `PDFView` object.
- [func takePasswordFrom(Any)](./pdfview/takepasswordfrom%28_%29.md)
  Unlocks with the password from the specified sender.
### Configuring Document View
- [Configurations](./configurations.md)
  Define display modes, scaling, rendering, printing and graphics properties.
### Interacting in a View
- [Document Interactions](./document-interactions.md)
  Handle selections, work with annotation actions, convert page and view points, and work with mouse events in a document.
### Navigating Within a Document
- [var currentPage: PDFPage?](./pdfview/currentpage.md)
  Returns the current page.
- [var currentDestination: PDFDestination?](./pdfview/currentdestination.md)
  Returns a `PDFDestination` object representing the current page and the current point in the view specified in page space.
- [var visiblePages: [PDFPage]](./pdfview/visiblepages.md)
  Returns an array of `PDFPage` objects that represent the currently visible pages.
- [Navigation](./navigation.md)
  Operations for moving through page history and seeking to a page in a document.
### Setting the Delegate
- [var delegate: (any PDFViewDelegate)?](./pdfview/delegate.md)
  Returns the view’s delegate.
- [protocol PDFViewDelegate](./pdfviewdelegate.md)
  The delegate for the `PDFView` object.
### Instance Properties
- [var findInteraction: UIFindInteraction](./pdfview/findinteraction.md)
- [var isFindInteractionEnabled: Bool](./pdfview/isfindinteractionenabled.md)
- [var isInMarkupMode: Bool](./pdfview/isinmarkupmode.md)
- [var pageOverlayViewProvider: (any PDFPageOverlayViewProvider)?](./pdfview/pageoverlayviewprovider.md)
- [var pageShadowsEnabled: Bool](./pdfview/pageshadowsenabled.md)
### Notifications
- [PDFViewChangedHistoryNotification](./pdfviewchangedhistorynotification.md)
  A notification posted when the page history changes.
- [PDFViewDocumentChangedNotification](./pdfviewdocumentchangednotification.md)
  A notification posted when a new document is associated with the view.
- [PDFViewPageChangedNotification](./pdfviewpagechangednotification.md)
  A notification posted when a new page becomes the current page.
- [PDFViewScaleChangedNotification](./pdfviewscalechangednotification.md)
  A notification posted when the scale factor changes.
- [PDFViewAnnotationHitNotification](./pdfviewannotationhitnotification.md)
  A notification posted when the user clicks on an annotation.
- [PDFViewCopyPermissionNotification](./pdfviewcopypermissionnotification.md)
  A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [PDFViewPrintPermissionNotification](./pdfviewprintpermissionnotification.md)
  A notification posted when the user attempts to print without the appropriate permissions.
- [PDFViewAnnotationWillHitNotification](./pdfviewannotationwillhitnotification.md)
  A notification posted before the user clicks an annotation.
- [PDFViewSelectionChangedNotification](./pdfviewselectionchangednotification.md)
  A notification posted when the current selection has changed.
- [PDFViewDisplayModeChangedNotification](./pdfviewdisplaymodechangednotification.md)
  A notification posted when the display mode has changed.
- [PDFViewDisplayBoxChangedNotification](./pdfviewdisplayboxchangednotification.md)
  A notification posted when the display box has changed.
- [PDFViewVisiblePagesChangedNotification](./pdfviewvisiblepageschangednotification.md)
  A notification posted when the visible pages have changed.

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
- [NSAnimationDelegate](../AppKit/nsanimationdelegate.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSMenuDelegate](../AppKit/nsmenudelegate.md)
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
- [UIFindInteractionDelegate](../UIKit/uifindinteractiondelegate.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIGestureRecognizerDelegate](../UIKit/uigesturerecognizerdelegate.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Views
- [class PDFThumbnailView](./pdfthumbnailview.md)
  An object that contains a set of thumbnails, each of which represents a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview)*