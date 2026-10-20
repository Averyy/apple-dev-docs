# init(fullName:phoneOrEmailAddress:leadingConfiguration:trailingConfiguration:detailText:trailingText:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list item that represents a contact.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(fullName: String, phoneOrEmailAddress: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)
```

```objc
- (instancetype) initWithFullName:(NSString *) fullName phoneOrEmailAddress:(NSString *) phoneOrEmailAddress leadingConfiguration:(CPMessageListItemLeadingConfiguration *) leadingConfiguration trailingConfiguration:(CPMessageListItemTrailingConfiguration *) trailingConfiguration detailText:(NSString *) detailText trailingText:(NSString *) trailingText;
```

## Parameters

- `fullName`: The contact’s full name. The list item displays this value as its primary content. Siri speaks this when the user selects the list item.
- `phoneOrEmailAddress`: The phone number or email address that Siri uses when launching the compose message flow.
- `leadingConfiguration`: The configuration that describes the visual elements of the list item’s leading region.
- `trailingConfiguration`: The configuration that describes the visual elements of the list item’s trailing region.
- `detailText`: The list item’s secondary text.
- `trailingText`: Supplementary text that the list item’s trailing region displays.

## See Also

### Creating a Message List Item
- [init(conversationIdentifier: String, text: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](./init%28conversationidentifier,text,leadingconfiguration,trailingconfiguration,detailtext,trailingtext%29.md)
  Creates a list item that represents an existing conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/init(fullname:phoneoremailaddress:leadingconfiguration:trailingconfiguration:detailtext:trailingtext:))*