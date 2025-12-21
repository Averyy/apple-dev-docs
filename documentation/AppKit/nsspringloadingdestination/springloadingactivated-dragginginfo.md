# springLoadingActivated(_:draggingInfo:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Responds to the activation or deactivation of spring-loading on a destination.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func springLoadingActivated(_ activated: Bool, draggingInfo: any NSDraggingInfo)
```

#### Discussion

Typically, spring-loading is fully activated when a hover timeout occurs or the user finishes force clicking on a destination object to initiate spring-loading. In these cases, the `springLoadingActivated:draggingInfo:` method is only called once with an `activated` parameter value of [`true`](https://developer.apple.com/documentation/Swift/true).

However, if the destination is configured with continuous activation (`NSSpringLoadingOptions` was set to `NSSpringLoadingContinuousActivation`), then the `springLoadingActivated:draggingInfo:` method is called twice. First, it’s called with an `activated` parameter value of [`true`](https://developer.apple.com/documentation/Swift/true) when a hover timeout occurs or the user begins force clicking on a destination object to initiate spring-loading. Then, it’s called again with an `activated` parameter value of [`false`](https://developer.apple.com/documentation/Swift/false) when the hover exits the destination’s bounds or the user finishes force clicking on the destination object.

## Parameters

- `activated`: A Boolean value indicating whether spring-loading has been activated on the destination.   indicates that spring-loading has been activated.   indicates that spring-loading has been deactivated.
- `draggingInfo`: An   object, which provides information about the drag event, including the dragged data.

## See Also

- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [struct NSSpringLoadingOptions](nsspringloadingoptions.md)
  These constants denote the type of spring-loading behavior configured for the destination object.
- [protocol NSDraggingInfo](nsdragginginfo.md)
  A set of methods that supply information about a dragging session.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/springloadingactivated(_:dragginginfo:))*