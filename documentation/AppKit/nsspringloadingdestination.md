# NSSpringLoadingDestination

**Framework**: AppKit  
**Kind**: protocol

A set of methods that the destination object (or recipient) of a dragged object can implement to support spring-loading.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSSpringLoadingDestination : NSObjectProtocol
```

#### Overview

Spring-loading is the act of dragging an object onto a destination object and hovering or force-clicking to activate the destination object A view can be configured as a drag-and-drop destination, a spring-loading destination, or both. If a view implements both drag-and-drop and spring-loading, then it will receive messages for both operations.

Note that the view beneath the cursor during a drag receives priority. For example, if a parent view implements drag-and-drop and a subview implements spring-loading, then the parent view will not receive drag-and-drop messages while the cursor is over the subview.

## Topics

### Respond to Spring-loading Events
- [func springLoadingActivated(Bool, draggingInfo: any NSDraggingInfo)](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md)
  Responds to the activation or deactivation of spring-loading on a destination.
- [func springLoadingHighlightChanged(any NSDraggingInfo)](nsspringloadingdestination/springloadinghighlightchanged(_:).md)
  Updates the destination’s user interface to display a new highlighting style during a spring-loading operation.
- [func springLoadingEntered(any NSDraggingInfo) -> NSSpringLoadingOptions](nsspringloadingdestination/springloadingentered(_:).md)
  Returns whether to enable or disable spring-loading when a drag enters the bounds of the spring-loading destination.
- [func springLoadingUpdated(any NSDraggingInfo) -> NSSpringLoadingOptions](nsspringloadingdestination/springloadingupdated(_:).md)
  Returns whether to enable or disable spring-loading as a drag moves within the bounds of the spring-loading destination or `draggingInfo` changes during the drag.
- [func springLoadingExited(any NSDraggingInfo)](nsspringloadingdestination/springloadingexited(_:).md)
  Responds when a drag exits the bounds of the spring-loading destination.
- [func draggingEnded(any NSDraggingInfo)](nsspringloadingdestination/draggingended(_:).md)
  Responds to the end of a drag operation.
### Constants
- [struct NSSpringLoadingOptions](nsspringloadingoptions.md)
  These constants denote the type of spring-loading behavior configured for the destination object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSDraggingDestination](nsdraggingdestination.md)
  A set of methods that the destination object (or recipient) of a dragged image must implement.
- [protocol NSDraggingInfo](nsdragginginfo.md)
  A set of methods that supply information about a dragging session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination)*