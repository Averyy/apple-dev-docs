# draggingEnded(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Responds to the end of a drag operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func draggingEnded(_ draggingInfo: any NSDraggingInfo)
```

```objc
- (void) draggingEnded:(id<NSDraggingInfo>) draggingInfo;
```

#### Discussion

This method is called when a drag operation has ended. If the destination object is both a dragging destination (class `NSDraggingDestination`) and a spring-loading destination (class `NSSpringLoadingDestination`), note that this method is only called once.

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
- [func springLoadingExited(any NSDraggingInfo)](./springloadingexited%28_%29.md)
  Responds when a drag exits the bounds of the spring-loading destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/draggingended(_:))*