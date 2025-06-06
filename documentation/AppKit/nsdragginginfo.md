# NSDraggingInfo

**Framework**: AppKit  
**Kind**: protocol

A set of methods that supply information about a dragging session.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSDraggingInfo : NSObjectProtocol
```

#### Overview

You invoke the [`NSDraggingInfo`](nsdragginginfo.md) protocol methods from within a class’s implementation of [`NSDraggingDestination`](nsdraggingdestination.md) methods. AppKit automatically passes an object that conforms to the [`NSDraggingInfo`](nsdragginginfo.md) protocol as the argument to each of the methods that [`NSDraggingDestination`](nsdraggingdestination.md) defines. Send [`NSDraggingInfo`](nsdragginginfo.md) messages to this object. You never need to create a class that implements the [`NSDraggingInfo`](nsdragginginfo.md) protocol.

## Topics

### Obtaining information about the dragging session
- [var draggingPasteboard: NSPasteboard](nsdragginginfo/draggingpasteboard.md)
  The pasteboard object that holds the dragged data.
- [var draggingSequenceNumber: Int](nsdragginginfo/draggingsequencenumber.md)
  A number that uniquely identifies the dragging session.
- [var draggingSource: Any?](nsdragginginfo/draggingsource.md)
  The source, or owner, of the dragged data.
- [var draggingSourceOperationMask: NSDragOperation](nsdragginginfo/draggingsourceoperationmask.md)
  Information about the dragging operation and the data it contains.
- [var draggingLocation: NSPoint](nsdragginginfo/dragginglocation.md)
  The current location of the mouse pointer in the base coordinate system of the destination object’s window.
- [var draggingDestinationWindow: NSWindow?](nsdragginginfo/draggingdestinationwindow.md)
  The destination window for the dragging operation.
- [var numberOfValidItemsForDrop: Int](nsdragginginfo/numberofvaliditemsfordrop.md)
  The number of valid items for a drop operation.
- [func namesOfPromisedFilesDropped(atDestination: URL) -> [String]?](nsdragginginfo/namesofpromisedfilesdropped(atdestination:).md)
  Sets the drop location for promised files and returns the names of the files that the receiver promises to create there.
### Getting image information
- [var draggedImageLocation: NSPoint](nsdragginginfo/draggedimagelocation.md)
  The current location of the dragged image’s origin, in the base coordinate system of the destination object’s window.
- [var draggedImage: NSImage?](nsdragginginfo/draggedimage.md)
  The image that represents the dragging item.
### Sliding the image
- [func slideDraggedImage(to: NSPoint)](nsdragginginfo/slidedraggedimage(to:).md)
  Slides the image to a specified location.
- [var animatesToDestination: Bool](nsdragginginfo/animatestodestination.md)
  A Boolean value that indicates whether the dragging formation animates while the drag is over the destination.
- [var draggingFormation: NSDraggingFormation](nsdragginginfo/draggingformation.md)
  The formation of the dragging items while the drag is over the destination.
### Enumerate dragged items
- [func enumerateDraggingItems(options: NSDraggingItemEnumerationOptions, for: NSView?, classes: [AnyClass], searchOptions: [NSPasteboard.ReadingOptionKey : Any], using: (NSDraggingItem, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](nsdragginginfo/enumeratedraggingitems(options:for:classes:searchoptions:using:).md)
  Enumerates through each dragging item.
### Implementing spring-loading support
- [var springLoadingHighlight: NSSpringLoadingHighlight](nsdragginginfo/springloadinghighlight.md)
  A highlighting style for your app’s user interface to display during a spring-loading operation.
- [func resetSpringLoading()](nsdragginginfo/resetspringloading.md)
  Resets a spring-loading operation to its initial state.
### Constants
- [struct NSDragOperation](nsdragoperation.md)
  A group of constants that represent which operations the dragging source can perform on dragging items.
- [struct NSDraggingItemEnumerationOptions](nsdraggingitemenumerationoptions.md)
  A group of constants that specify options to use when enumerating dragging items.
- [enum NSSpringLoadingHighlight](nsspringloadinghighlight.md)
  A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.
- [enum NSDraggingFormation](nsdraggingformation.md)
  Constants that control the visual format of multiple dragging items.
- [enum NSDraggingContext](nsdraggingcontext.md)
  Constants that specify whether a drag terminates within or outside the application.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSDraggingDestination](nsdraggingdestination.md)
  A set of methods that the destination object (or recipient) of a dragged image must implement.
- [protocol NSSpringLoadingDestination](nsspringloadingdestination.md)
  A set of methods that the destination object (or recipient) of a dragged object can implement to support spring-loading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo)*