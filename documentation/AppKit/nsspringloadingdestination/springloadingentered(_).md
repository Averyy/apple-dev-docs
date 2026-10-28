# springLoadingEntered(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whether to enable or disable spring-loading when a drag enters the bounds of the spring-loading destination.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func springLoadingEntered(_ draggingInfo: any NSDraggingInfo) -> NSSpringLoadingOptions
```

```objc
- (NSSpringLoadingOptions) springLoadingEntered:(id<NSDraggingInfo>) draggingInfo;
```

## Return Value

A value of type `NSSpringLoadingOptions` to enable or disable spring-loading. Returning a value of `NSSpringLoadingEnabled` enables typical spring-loading behavior that is appropriate in most cases.

## Discussion

This method is called when a drag enters the bounds of the spring-loading destination. It returns a value of type `NSSpringLoadingOptions` to enable or disable spring-loading for the destination.

This method provides an opportunity to perform work in preparation for spring-loading becoming engaged.

Note that you *must* implement either this method or [`springLoadingUpdated(_:)`](./springloadingupdated%28_%29.md) to enable spring-loading.

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
- [func springLoadingUpdated(any NSDraggingInfo) -> NSSpringLoadingOptions](./springloadingupdated%28_%29.md)
  Returns whether to enable or disable spring-loading as a drag moves within the bounds of the spring-loading destination or `draggingInfo` changes during the drag.
- [func springLoadingExited(any NSDraggingInfo)](./springloadingexited%28_%29.md)
  Responds when a drag exits the bounds of the spring-loading destination.
- [func draggingEnded(any NSDraggingInfo)](./draggingended%28_%29.md)
  Responds to the end of a drag operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadingdestination/springloadingentered(_:))*