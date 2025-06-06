# draggingEnded(_:)

**Framework**: AppKit  
**Kind**: method

Responds to the end of a drag operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func draggingEnded(_ draggingInfo: any NSDraggingInfo)
```

#### Discussion

This method is called when a drag operation has ended. If the destination object is both a dragging destination (class `NSDraggingDestination`) and a spring-loading destination (class `NSSpringLoadingDestination`), note that this method is only called once.

## Parameters

- `draggingInfo`: An object of type  , which provides information about the drag event, including the dragged data.

## See Also

- [struct NSSpringLoadingOptions](nsspringloadingoptions.md)
  These constants denote the type of spring-loading behavior configured for the destination object.
- [protocol NSDraggingInfo](nsdragginginfo.md)
  A set of methods that supply information about a dragging session.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/draggingended(_:))*