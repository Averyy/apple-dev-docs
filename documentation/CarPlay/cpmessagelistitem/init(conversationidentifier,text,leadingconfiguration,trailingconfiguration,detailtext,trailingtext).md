# init(conversationIdentifier:text:leadingConfiguration:trailingConfiguration:detailText:trailingText:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a list item that represents an existing conversation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(conversationIdentifier: String, text: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)
```

```objc
- (instancetype) initWithConversationIdentifier:(NSString *) conversationIdentifier text:(NSString *) text leadingConfiguration:(CPMessageListItemLeadingConfiguration *) leadingConfiguration trailingConfiguration:(CPMessageListItemTrailingConfiguration *) trailingConfiguration detailText:(NSString *) detailText trailingText:(NSString *) trailingText;
```

## Parameters

- `conversationIdentifier`: Your app’s unique identifier for the conversation. Siri passes this value to your app when the user selects the list item.
- `text`: The conversation’s content. Siri speaks this when the user selects the list item.
- `leadingConfiguration`: The configuration that describes the visual elements of the list item’s leading region.
- `trailingConfiguration`: The configuration that describes the visual elements of the list item’s trailing region.
- `detailText`: The list item’s secondary text.
- `trailingText`: Supplementary text that the list item’s trailing region displays.

## See Also

### Creating a Message List Item
- [init(fullName: String, phoneOrEmailAddress: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](./init%28fullname,phoneoremailaddress,leadingconfiguration,trailingconfiguration,detailtext,trailingtext%29.md)
  Creates a list item that represents a contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/init(conversationidentifier:text:leadingconfiguration:trailingconfiguration:detailtext:trailingtext:))*