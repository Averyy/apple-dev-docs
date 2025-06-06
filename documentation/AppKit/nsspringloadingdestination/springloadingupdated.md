# springLoadingUpdated(_:)

**Framework**: AppKit  
**Kind**: method

Returns whether to enable or disable spring-loading as a drag moves within the bounds of the spring-loading destination or `draggingInfo` changes during the drag.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func springLoadingUpdated(_ draggingInfo: any NSDraggingInfo) -> NSSpringLoadingOptions
```

#### Return Value

A value of type `NSSpringLoadingOptions` to enable or disable spring-loading. A value of `NSSpringLoadingEnabled` enables typical spring-loading behavior.

#### Discussion

This method is called periodically as a drag changes position within the bounds of a spring-loaded destination or the `draggingInfo` changes during the drag. It returns a value of type `NSSpringLoadingOptions` to enable or disable spring-loading for the destination. If this method is not implemented, then spring-loading is enabled or disabled for the destination based on the return value of the `springLoadingEntered:` method.

Note that you  implement either this method or [`springLoadingEntered(_:)`](nsspringloadingdestination/springloadingentered(_:).md) to enable spring-loading.

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
- [func springLoadingExited(any NSDraggingInfo)](nsspringloadingdestination/springloadingexited(_:).md)
  Responds when a drag exits the bounds of the spring-loading destination.
- [func draggingEnded(any NSDraggingInfo)](nsspringloadingdestination/draggingended(_:).md)
  Responds to the end of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/springloadingupdated(_:))*