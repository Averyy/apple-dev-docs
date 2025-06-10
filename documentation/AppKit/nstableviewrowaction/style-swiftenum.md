# NSTableViewRowAction.Style

**Framework**: AppKit  
**Kind**: enum

Constants that help define the appearance and behavior of action buttons.

**Availability**:
- macOS 10.11+

## Declaration

```swift
enum Style
```

## Topics

### Constants
- [NSTableViewRowAction.Style.regular](nstableviewrowaction/style-swift.enum/regular.md)
  Apply the default style to the button. This style does not apply any special coloring to the button.
- [NSTableViewRowAction.Style.destructive](nstableviewrowaction/style-swift.enum/destructive.md)
  Apply a style that indicates that the action might change or delete data. This style changes the value of the [`backgroundColor`](nstableviewrowaction/backgroundcolor.md) property to an appropriate value to reflect the destructive action. After creating the action object, you can change the background color as needed. Destructive actions require a longer swipe to activate, and trigger an animation when a table row is deleted.
### Initializers
- [init?(rawValue: Int)](nstableviewrowaction/style-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction/style-swift.enum)*