# UIContextualAction.Style

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the style information that applies to the action button.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Style
```

```c
enum UIContextualActionStyle : NSInteger;
```

## Topics

### Styles
- [UIContextualAction.Style.normal](./style-swift.enum/normal.md)
  A normal action.
- [UIContextualAction.Style.destructive](./style-swift.enum/destructive.md)
  An action that deletes data or performs some type of destructive task.
### Initializers
- [init?(rawValue: Int)](./style-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the configuration details
- [var handler: UIContextualAction.Handler](./handler-swift.property.md)
  The handler block to execute when the user selects the action.
- [UIContextualAction.Handler](./handler-swift.typealias.md)
  The handler block to call in response to the selection of an action.
- [var style: UIContextualAction.Style](./style-swift.property.md)
  The style that applies to the action button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontextualaction/style-swift.enum)*