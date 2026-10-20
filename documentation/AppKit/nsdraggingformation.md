# NSDraggingFormation

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that control the visual format of multiple dragging items.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum NSDraggingFormation
```

```c
enum NSDraggingFormation : NSInteger;
```

## Topics

### Constants
- [NSDraggingFormation.default](./nsdraggingformation/default.md)
  A constant that represents the system determined formation.
- [NSDraggingFormation.none](./nsdraggingformation/none.md)
  A constant that represents no custom formation, so drag images maintain their set positions relative to each other.
- [NSDraggingFormation.pile](./nsdraggingformation/pile.md)
  A constant that represents a pile formation, so drag images display on top of each other with random rotations.
- [NSDraggingFormation.list](./nsdraggingformation/list.md)
  A constant that represents a list formation, so drag images display vertically, non-overlapping with the left edges aligned.
- [NSDraggingFormation.stack](./nsdraggingformation/stack.md)
  A constant that represents a stack formation, so drag images display overlapping diagonally.
### Initializers
- [init?(rawValue: Int)](./nsdraggingformation/init%28rawvalue%29.md)

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
- [enum NSDraggingContext](./nsdraggingcontext.md)
  Constants that specify whether a drag terminates within or outside the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingformation)*