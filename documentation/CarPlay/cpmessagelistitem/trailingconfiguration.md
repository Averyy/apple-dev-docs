# trailingConfiguration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The configuration of the list item’s trailing region.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var trailingConfiguration: CPMessageListItemTrailingConfiguration? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPMessageListItemTrailingConfiguration * trailingConfiguration;
```

## Discussion

An instance of [`CPMessageListItemTrailingConfiguration`](../cpmessagelistitemtrailingconfiguration.md) that describes the visual elements of the list item’s trailing region. The region can show a [`CPMessageTrailingItem`](../cpmessagetrailingitem.md) and an image.

## See Also

### Managing Leading and Trailing Configurations
- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](./leadingconfiguration.md)
  The configuration of the list item’s leading region.
- [class CPMessageListItemLeadingConfiguration](../cpmessagelistitemleadingconfiguration.md)
  An object that describes the appearance of a message list item’s leading region.
- [class CPMessageListItemTrailingConfiguration](../cpmessagelistitemtrailingconfiguration.md)
  An object that describes the appearance of a message list item’s trailing region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/trailingconfiguration)*