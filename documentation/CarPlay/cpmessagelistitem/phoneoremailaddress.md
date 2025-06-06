# phoneOrEmailAddress

**Framework**: CarPlay  
**Kind**: property

The contact’s phone number or email address.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var phoneOrEmailAddress: String? { get set }
```

#### Discussion

When the user selects the list item, Siri launches the message compose flow and uses this property’s value as the recipient’s contact information.

## See Also

- [var conversationIdentifier: String?](cpmessagelistitem/conversationidentifier.md)
  The conversation’s unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/phoneoremailaddress)*