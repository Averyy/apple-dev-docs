# PDFThumbnailView

**Framework**: PDFKit  
**Kind**: class

An object that contains a set of thumbnails, each of which represents a page in a PDF document.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PDFThumbnailView
```

## Topics

### Accessing the Associated PDF View
- [var pdfView: PDFView?](pdfthumbnailview/pdfview.md)
  Returns the `PDFView` object associated with the thumbnail view.
### Managing the Size of a Thumbnail View
- [var thumbnailSize: CGSize](pdfthumbnailview/thumbnailsize.md)
  Returns the maximum width and height of the thumbnails in the thumbnail view.
### Working with Thumbnail View Display Characteristics
- [var maximumNumberOfColumns: Int](pdfthumbnailview/maximumnumberofcolumns.md)
  Returns the maximum number of columns of thumbnails the thumbnail view can display.
- [var labelFont: NSFont?](pdfthumbnailview/labelfont.md)
  Returns the font used to label the thumbnails.
- [var backgroundColor: UIColor?](pdfthumbnailview/backgroundcolor.md)
  Returns the color used in the background of the thumbnail view.
### Managing the Behavior of a Thumbnail View
- [var allowsDragging: Bool](pdfthumbnailview/allowsdragging.md)
  Returns a Boolean value indicating whether users can drag thumbnails (that is, re-order pages in the document) within the thumbnail view.
- [var allowsMultipleSelection: Bool](pdfthumbnailview/allowsmultipleselection.md)
  Returns a Boolean value indicating whether users can select multiple thumbnails in the thumbnail view at one time.
- [var selectedPages: [PDFPage]?](pdfthumbnailview/selectedpages.md)
  Returns an array of PDF pages that correspond to the selected thumbnails in the thumbnail view.
### Instance Properties
- [var contentInset: UIEdgeInsets](pdfthumbnailview/contentinset.md)
- [var layoutMode: PDFThumbnailLayoutMode](pdfthumbnailview/layoutmode.md)

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
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
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

- [class PDFView](pdfview.md)
  An object that encapsulates the functionality of PDF Kit into a single widget that you can add to your application using Interface Builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview)*