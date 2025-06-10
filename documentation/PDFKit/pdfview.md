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
@MainActor
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
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAnimationDelegate](../AppKit/NSAnimationDelegate.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSMenuDelegate](../AppKit/NSMenuDelegate.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFindInteractionDelegate](../UIKit/UIFindInteractionDelegate.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIGestureRecognizerDelegate](../UIKit/UIGestureRecognizerDelegate.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class PDFThumbnailView](pdfthumbnailview.md)
  An object that contains a set of thumbnails, each of which represents a page in a PDF document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfview)*