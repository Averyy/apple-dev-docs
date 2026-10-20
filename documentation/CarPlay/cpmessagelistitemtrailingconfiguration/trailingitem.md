# trailingItem

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The configuration’s item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var trailingItem: CPMessageTrailingItem { get }
```

```objc
@property (nonatomic, readonly) CPMessageTrailingItem trailingItem;
```

#### Discussion

Configurations are immutable. To change or remove the item that the message list item’s trailing region shows, create a new configuration and update the list item’s [`trailingConfiguration`](../cpmessagelistitem/trailingconfiguration.md) property.

## See Also

### Getting the Trailing Item
- [enum CPMessageTrailingItem](../cpmessagetrailingitem.md)
  The accessories that a message list item can display in its trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemtrailingconfiguration/trailingitem)*