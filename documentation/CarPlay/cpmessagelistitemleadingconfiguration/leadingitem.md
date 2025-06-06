# leadingItem

**Framework**: CarPlay  
**Kind**: property

The configuration’s item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var leadingItem: CPMessageLeadingItem { get }
```

#### Discussion

Configurations are immutable. To change or remove the item that the message list item’s leading region shows, create a new configuration and update the list item’s [`leadingConfiguration`](cpmessagelistitem/leadingconfiguration.md) property.

## See Also

- [enum CPMessageLeadingItem](cpmessageleadingitem.md)
  The accessories that a message list item can display in its leading region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemleadingconfiguration/leadingitem)*