# springLoadingHighlight

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

A highlighting style for your app’s user interface to display during a spring-loading operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var springLoadingHighlight: NSSpringLoadingHighlight { get }
```

#### Discussion

During a spring-loaded operation, a destination may initiate animated highlighting to visually cue the user that spring-loading has been engaged or disengaged.

This property contains a highlight style of class [`NSSpringLoadingHighlight`](nsspringloadinghighlight.md)—no highlight, standard highlight, or emphasized highlight. Use this value to update your destination’s user interface accordingly to reflect the appropriate highlight style.

> ❗ **Important**:  Do not use highlighting as a means to determine whether spring-loading has actually been activated or deactivated. The [`springLoadingActivated(_:draggingInfo:)`](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md) method alerts your app when spring-loading activation occurs.

 Do not use highlighting as a means to determine whether spring-loading has actually been activated or deactivated. The [`springLoadingActivated(_:draggingInfo:)`](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md) method alerts your app when spring-loading activation occurs.

## See Also

- [func springLoadingHighlightChanged(any NSDraggingInfo)](nsspringloadingdestination/springloadinghighlightchanged(_:).md)
  Updates the destination’s user interface to display a new highlighting style during a spring-loading operation.
- [enum NSSpringLoadingHighlight](nsspringloadinghighlight.md)
  A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.
- [protocol NSSpringLoadingDestination](nsspringloadingdestination.md)
  A set of methods that the destination object (or recipient) of a dragged object can implement to support spring-loading.
- [func resetSpringLoading()](nsdragginginfo/resetspringloading.md)
  Resets a spring-loading operation to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdragginginfo/springloadinghighlight)*