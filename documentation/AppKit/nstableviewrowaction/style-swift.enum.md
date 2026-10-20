# NSTableViewRowAction.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that help define the appearance and behavior of action buttons.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum Style
```

```c
enum NSTableViewRowActionStyle : NSInteger;
```

## Topics

### Constants
- [NSTableViewRowAction.Style.regular](./style-swift.enum/regular.md)
  Apply the default style to the button. This style does not apply any special coloring to the button.
- [NSTableViewRowAction.Style.destructive](./style-swift.enum/destructive.md)
  Apply a style that indicates that the action might change or delete data. This style changes the value of the [`backgroundColor`](./backgroundcolor.md) property to an appropriate value to reflect the destructive action. After creating the action object, you can change the background color as needed. Destructive actions require a longer swipe to activate, and trigger an animation when a table row is deleted.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction/style-swift.enum)*