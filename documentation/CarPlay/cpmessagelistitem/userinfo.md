# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Custom information you want to store with the message list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

## Discussion

Store any app-specific data for the item in this property. For example, store the unique ID of the conversation or contact object. The item maintains a strong reference to the object you specify.

## See Also

### Configuring additional details
- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](./leadingconfiguration.md)
  Additional content to display at the leading edge of the row.
- [var trailingConfiguration: CPMessageListItemTrailingConfiguration?](./trailingconfiguration.md)
  Additional content to display at the trailing edge of the row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/userinfo)*