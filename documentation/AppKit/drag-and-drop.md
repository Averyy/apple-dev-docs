# Drag and Drop

**Framework**: Appkit

Support the direct manipulation of your app’s content using drag and drop.

#### Overview

With very little programming on your part, custom-view objects can be dragged and dropped anywhere. Objects become part of this dragging mechanism by conforming to dragging protocols: Draggable objects conform to the [`NSDraggingSource`](nsdraggingsource.md) protocol, and destination objects (that is, receivers of a drop) conform to the [`NSDraggingDestination`](nsdraggingdestination.md) protocol. AppKit hides all the details of tracking the cursor and displaying the dragged image.

> **Note**:  To learn how to adopt drag and drop in your iOS app, see [`Drag and drop`](https://developer.apple.com/documentation/UIKit/drag-and-drop).

To learn how to use drag and drop for an image view, see [`Supporting Drag and Drop Through File Promises`](supporting-drag-and-drop-through-file-promises.md). To use drag and drop in a table view, see [`Supporting Table View Drag and Drop Through File Promises`](supporting-table-view-drag-and-drop-through-file-promises.md). For an example of drag and drop in a collection view, see [`Supporting Collection View Drag and Drop Through File Promises`](supporting-collection-view-drag-and-drop-through-file-promises.md), and for an outline view: [`Navigating Hierarchical Data Using Outline and Split Views`](navigating-hierarchical-data-using-outline-and-split-views.md).

## Topics

### Drag Sources
- [protocol NSDraggingSource](nsdraggingsource.md)
  A set of methods that are implemented by the source object in a dragging session.
- [class NSDraggingItem](nsdraggingitem.md)
  A single dragged item within a dragging session.
- [class NSDraggingSession](nsdraggingsession.md)
  The encapsulation of a drag-and-drop action that supports modification of the drag while in progress.
- [class NSDraggingImageComponent](nsdraggingimagecomponent.md)
  A single object in a dragging item.
### Drop Targets
- [protocol NSDraggingDestination](nsdraggingdestination.md)
  A set of methods that the destination object (or recipient) of a dragged image must implement.
- [protocol NSDraggingInfo](nsdragginginfo.md)
  A set of methods that supply information about a dragging session.
- [protocol NSSpringLoadingDestination](nsspringloadingdestination.md)
  A set of methods that the destination object (or recipient) of a dragged object can implement to support spring-loading.

## See Also

- [Mouse, Keyboard, and Trackpad](mouse-keyboard-and-trackpad.md)
  Handle events related to mouse, keyboard, and trackpad input.
- [Menus, Cursors, and the Dock](menus-cursors-and-the-dock.md)
  Implement menus and cursors to facilitate interactions with your app, and use your app’s Dock tile to convey updated information.
- [Gestures](gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Touch Bar](touch-bar.md)
  Display interactive content and controls in the Touch Bar.
- [Accessibility for AppKit](accessibility-for-appkit.md)
  Make your AppKit apps accessible to everyone who uses macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/drag-and-drop)*