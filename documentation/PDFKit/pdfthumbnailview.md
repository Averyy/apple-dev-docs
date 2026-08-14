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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
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

- [class PDFView](pdfview.md)
  An object that encapsulates the functionality of PDF Kit into a single widget that you can add to your application using Interface Builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview)*