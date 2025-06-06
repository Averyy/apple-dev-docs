# NSSpringLoadingHighlight

**Framework**: AppKit  
**Kind**: enum

A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum NSSpringLoadingHighlight
```

#### Overview

The [`springLoadingHighlight`](nsdragginginfo/springloadinghighlight.md) method provides one of these constant values.

Do not use highlighting as a means to determine whether spring-loading has actually been activated or deactivated. The [`springLoadingActivated(_:draggingInfo:)`](nsspringloadingdestination/springloadingactivated(_:dragginginfo:).md) method alerts your app when spring-loading activation occurs.

## Topics

### Constants
- [NSSpringLoadingHighlight.none](nsspringloadinghighlight/none.md)
  A constant that indicates no highlighting.
- [NSSpringLoadingHighlight.standard](nsspringloadinghighlight/standard.md)
  A constant that indicates standard highlighting to show the destination supports spring-loading.
- [NSSpringLoadingHighlight.emphasized](nsspringloadinghighlight/emphasized.md)
  A constant that indicates emphasized highlighting to show active spring-loading on the destination.
### Initializers
- [init?(rawValue: Int)](nsspringloadinghighlight/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct NSDragOperation](nsdragoperation.md)
  A group of constants that represent which operations the dragging source can perform on dragging items.
- [struct NSDraggingItemEnumerationOptions](nsdraggingitemenumerationoptions.md)
  A group of constants that specify options to use when enumerating dragging items.
- [enum NSDraggingFormation](nsdraggingformation.md)
  Constants that control the visual format of multiple dragging items.
- [enum NSDraggingContext](nsdraggingcontext.md)
  Constants that specify whether a drag terminates within or outside the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspringloadinghighlight)*