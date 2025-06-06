# springLoadingHighlightChanged(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Updates the destination’s user interface to display a new highlighting style during a spring-loading operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func springLoadingHighlightChanged(_ draggingInfo: any NSDraggingInfo)
```

#### Discussion

During a spring-loaded operation, a destination may initiate animated highlighting to visually cue the user that spring-loading has been engaged or disengaged. This method is called as different stages of this animation are reached, providing an opportunity to change the highlighting style. Check the `springLoadingHighlight` property of the `draggingInfo` object to determine the style of highlighting to apply. Then, update the destination’s user interface accordingly.

> ❗ **Important**:  Do not use highlighting as a means to determine whether spring-loading has actually been activated or deactivated. The [`springLoadingActivated(_:draggingInfo:)`](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md) method alerts your app when spring-loading activation occurs.

 Do not use highlighting as a means to determine whether spring-loading has actually been activated or deactivated. The [`springLoadingActivated(_:draggingInfo:)`](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md) method alerts your app when spring-loading activation occurs.

## Parameters

- `draggingInfo`: An object of type  , which provides information about the drag event, including a highlighting style to apply.

## See Also

- [struct NSDragOperation](nsdragoperation.md)
  A group of constants that represent which operations the dragging source can perform on dragging items.
- [struct NSSpringLoadingOptions](nsspringloadingoptions.md)
  These constants denote the type of spring-loading behavior configured for the destination object.
- [protocol NSDraggingInfo](nsdragginginfo.md)
  A set of methods that supply information about a dragging session.
- [func springLoadingActivated(Bool, draggingInfo: any NSDraggingInfo)](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md)
  Responds to the activation or deactivation of spring-loading on a destination.
- [func springLoadingEntered(any NSDraggingInfo) -> NSSpringLoadingOptions](nsspringloadingdestination/springloadingentered(_:).md)
  Returns whether to enable or disable spring-loading when a drag enters the bounds of the spring-loading destination.
- [func springLoadingUpdated(any NSDraggingInfo) -> NSSpringLoadingOptions](nsspringloadingdestination/springloadingupdated(_:).md)
  Returns whether to enable or disable spring-loading as a drag moves within the bounds of the spring-loading destination or `draggingInfo` changes during the drag.
- [func springLoadingExited(any NSDraggingInfo)](nsspringloadingdestination/springloadingexited(_:).md)
  Responds when a drag exits the bounds of the spring-loading destination.
- [func draggingEnded(any NSDraggingInfo)](nsspringloadingdestination/draggingended(_:).md)
  Responds to the end of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/springloadinghighlightchanged(_:))*