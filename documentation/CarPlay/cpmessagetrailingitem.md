# CPMessageTrailingItem

**Framework**: CarPlay  
**Kind**: enum

The accessories that a message list item can display in its trailing region.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum CPMessageTrailingItem
```

#### Overview

Use these constants when creating instances of [`CPMessageListItemTrailingConfiguration`](cpmessagelistitemtrailingconfiguration.md). A trailing item can provide additional context for a list item’s contents, or help communicate its behavior.

## Topics

### Trailing Items
- [CPMessageTrailingItem.none](cpmessagetrailingitem/none.md)
  Don’t show a trailing item.
- [CPMessageTrailingItem.mute](cpmessagetrailingitem/mute.md)
  Show a muted speaker icon.
### Initializers
- [init?(rawValue: Int)](cpmessagetrailingitem/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var trailingItem: CPMessageTrailingItem](cpmessagelistitemtrailingconfiguration/trailingitem.md)
  The configuration’s item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagetrailingitem)*