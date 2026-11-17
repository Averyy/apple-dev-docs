# trailingConfiguration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional content to display at the trailing edge of the row.

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

This property specifies visual elements to display after the row text. For example, you can tell CarPlay to display a mute button or a custom image.

## See Also

### Configuring additional details
- [var leadingConfiguration: CPMessageListItemLeadingConfiguration](./leadingconfiguration.md)
  Additional content to display at the leading edge of the row.
- [var userInfo: Any?](./userinfo.md)
  Custom information you want to store with the message list item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/trailingconfiguration)*