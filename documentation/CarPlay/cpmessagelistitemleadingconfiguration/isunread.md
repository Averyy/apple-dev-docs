# isUnread

**Framework**: CarPlay  
**Kind**: property

A Boolean value that determines whether the message list item displays an unread indicator.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isUnread: Bool { get }
```

#### Discussion

Configurations are immutable. To toggle the message list item’s unread indicator, create a new configuration and update the list item’s [`leadingConfiguration`](cpmessagelistitem/leadingconfiguration.md) property.

## See Also

- [var leadingImage: UIImage?](cpmessagelistitemleadingconfiguration/leadingimage.md)
  The configuration’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitemleadingconfiguration/isunread)*