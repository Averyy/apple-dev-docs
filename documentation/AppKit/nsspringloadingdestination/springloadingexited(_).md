# springLoadingExited(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Responds when a drag exits the bounds of the spring-loading destination.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func springLoadingExited(_ draggingInfo: any NSDraggingInfo)
```

```objc
- (void) springLoadingExited:(id<NSDraggingInfo>) draggingInfo;
```

#### Discussion

This method is called when a drag exits the bounds of a spring-loaded destination.

This is a good place to clean up any initialization work that may have been performed during [`springLoadingEntered(_:)`](./springloadingentered%28_%29.md).

## Parameters

- `draggingInfo`: An object of type `NSDraggingInfo`, which provides information about the drag event, including the dragged data.

## See Also

### Related Documentation
- [struct NSSpringLoadingOptions](../nsspringloadingoptions.md)
  These constants denote the type of spring-loading behavior configured for the destination object.
- [protocol NSDraggingInfo](../nsdragginginfo.md)
  A set of methods that supply information about a dragging session.
### Respond to Spring-loading Events
- [func springLoadingActivated(Bool, draggingInfo: any NSDraggingInfo)](./springloadingactivated%28_,dragginginfo%29.md)
  Responds to the activation or deactivation of spring-loading on a destination.
- [func springLoadingHighlightChanged(any NSDraggingInfo)](./springloadinghighlightchanged%28_%29.md)
  Updates the destination’s user interface to display a new highlighting style during a spring-loading operation.
- [func springLoadingEntered(any NSDraggingInfo) -> NSSpringLoadingOptions](./springloadingentered%28_%29.md)
  Returns whether to enable or disable spring-loading when a drag enters the bounds of the spring-loading destination.
- [func springLoadingUpdated(any NSDraggingInfo) -> NSSpringLoadingOptions](./springloadingupdated%28_%29.md)
  Returns whether to enable or disable spring-loading as a drag moves within the bounds of the spring-loading destination or `draggingInfo` changes during the drag.
- [func draggingEnded(any NSDraggingInfo)](./draggingended%28_%29.md)
  Responds to the end of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/springloadingexited(_:))*