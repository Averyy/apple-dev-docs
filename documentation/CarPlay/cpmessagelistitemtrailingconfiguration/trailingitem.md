# trailingItem

**Framework**: CarPlay  
**Kind**: property

The configuration’s item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var trailingItem: CPMessageTrailingItem { get }
```

#### Discussion

Configurations are immutable. To change or remove the item that the message list item’s trailing region shows, create a new configuration and update the list item’s [`trailingConfiguration`](cpmessagelistitem/trailingconfiguration.md) property.

## See Also

- [enum CPMessageTrailingItem](cpmessagetrailingitem.md)
  The accessories that a message list item can display in its trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemtrailingconfiguration/trailingitem)*