# init(fullName:phoneOrEmailAddress:leadingConfiguration:trailingConfiguration:detailText:trailingText:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a message list item with the identifier for one of your app’s conversations.

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

## Return Value

An initialized message list item to add to your list content.

## Discussion

Use this initializer to create a row that represents a conversation with one or more people.

## Parameters

- `fullName`: The full name of the contact. CarPlay displays this text prominently in the row. When someone selects the row, Siri speaks this name as part of the workflow for composing a message.
- `phoneOrEmailAddress`: The contact’s phone or email address. Siri composes a message that targets the value you provide. CarPlay doesn’t display this text in the row.
- `leadingConfiguration`: Configuration options for the leading edge of the row.
- `trailingConfiguration`: Configuration options for the trailing edge of the row.
- `detailText`: Additional text to display below the main text string. Specify `nil` to omit this string from the row.
- `trailingText`: Additional text to display at the trailing edge of the row. Specify `nil` to omit this string from the row.

## See Also

### Creating a message list item
- [init(conversationIdentifier: String, text: String, leadingConfiguration: CPMessageListItemLeadingConfiguration, trailingConfiguration: CPMessageListItemTrailingConfiguration?, detailText: String?, trailingText: String?)](./init%28conversationidentifier,text,leadingconfiguration,trailingconfiguration,detailtext,trailingtext%29.md)
  Creates a message list item with the identifier for one of your app’s conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/init(fullname:phoneoremailaddress:leadingconfiguration:trailingconfiguration:detailtext:trailingtext:))*