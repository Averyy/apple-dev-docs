# PDFThumbnailView

**Framework**: PDFKit  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface PDFThumbnailView : UIView
```

*macOS*

```objc
@interface PDFThumbnailView : NSView
```

## Topics

### Accessing the Associated PDF View
- [var pdfView: PDFView?](./pdfthumbnailview/pdfview.md)
  Returns the `PDFView` object associated with the thumbnail view.
### Managing the Size of a Thumbnail View
- [var thumbnailSize: CGSize](./pdfthumbnailview/thumbnailsize.md)
  Returns the maximum width and height of the thumbnails in the thumbnail view.
### Working with Thumbnail View Display Characteristics
- [var maximumNumberOfColumns: Int](./pdfthumbnailview/maximumnumberofcolumns.md)
  Returns the maximum number of columns of thumbnails the thumbnail view can display.
- [var labelFont: NSFont?](./pdfthumbnailview/labelfont.md)
  Returns the font used to label the thumbnails.
- [var backgroundColor: UIColor?](./pdfthumbnailview/backgroundcolor.md)
  Returns the color used in the background of the thumbnail view.
### Managing the Behavior of a Thumbnail View
- [var allowsDragging: Bool](./pdfthumbnailview/allowsdragging.md)
  Returns a Boolean value indicating whether users can drag thumbnails (that is, re-order pages in the document) within the thumbnail view.
- [var allowsMultipleSelection: Bool](./pdfthumbnailview/allowsmultipleselection.md)
  Returns a Boolean value indicating whether users can select multiple thumbnails in the thumbnail view at one time.
- [var selectedPages: [PDFPage]?](./pdfthumbnailview/selectedpages.md)
  Returns an array of PDF pages that correspond to the selected thumbnails in the thumbnail view.
### Instance Properties
- [var contentInset: UIEdgeInsets](./pdfthumbnailview/contentinset.md)
- [var layoutMode: PDFThumbnailLayoutMode](./pdfthumbnailview/layoutmode.md)

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

## See Also

### Views
- [class PDFView](./pdfview.md)
  An object that encapsulates the functionality of PDF Kit into a single widget that you can add to your application using Interface Builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfthumbnailview)*