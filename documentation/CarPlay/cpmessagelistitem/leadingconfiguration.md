# leadingConfiguration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional content to display at the leading edge of the row.

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

This property specifies visual elements to display before the row text. For example, you can tell CarPlay to display an unread indicator or a custom image.

## See Also

### Configuring additional details
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](./trailingconfiguration.md)
  Additional content to display at the trailing edge of the row.
- [var userInfo: Any?](./userinfo.md)
  Custom information you want to store with the message list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/leadingconfiguration)*