# NSDraggingContext

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify whether a drag terminates within or outside the application.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum NSDraggingContext
```

```c
enum NSDraggingContext : NSInteger;
```

## Topics

### Constants
- [NSDraggingContext.outsideApplication](./nsdraggingcontext/outsideapplication.md)
  A constant that indicates dragging terminates outside the application.
- [NSDraggingContext.withinApplication](./nsdraggingcontext/withinapplication.md)
  A constant that indicates dragging terminates within the application.
### Initializers
- [init?(rawValue: Int)](./nsdraggingcontext/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct NSDragOperation](./nsdragoperation.md)
  A group of constants that represent which operations the dragging source can perform on dragging items.
- [struct NSDraggingItemEnumerationOptions](./nsdraggingitemenumerationoptions.md)
  A group of constants that specify options to use when enumerating dragging items.
- [enum NSSpringLoadingHighlight](./nsspringloadinghighlight.md)
  A group of constants that indicate a highlighting style for your app’s user interface to display during a spring-loading operation.
- [enum NSDraggingFormation](./nsdraggingformation.md)
  Constants that control the visual format of multiple dragging items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingcontext)*