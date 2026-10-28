# leadingConfiguration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The configuration of the list item’s leading region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var leadingConfiguration: CPMessageListItemLeadingConfiguration { get set }
```

```objc
@property (nonatomic, strong) CPMessageListItemLeadingConfiguration * leadingConfiguration;
```

## Discussion

An instance of [`CPMessageListItemLeadingConfiguration`](../cpmessagelistitemleadingconfiguration.md) that describes the visual elements of the list item’s leading region. The region can show a [`CPMessageLeadingItem`](../cpmessageleadingitem.md), an image, and an unread indicator.

## See Also

### Managing Leading and Trailing Configurations
- [class CPMessageListItemLeadingConfiguration](../cpmessagelistitemleadingconfiguration.md)
  An object that describes the appearance of a message list item’s leading region.
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](./trailingconfiguration.md)
  The configuration of the list item’s trailing region.
- [class CPMessageListItemTrailingConfiguration](../cpmessagelistitemtrailingconfiguration.md)
  An object that describes the appearance of a message list item’s trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/leadingconfiguration)*