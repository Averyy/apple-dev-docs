# SMSContent

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that holds the content of an SMS message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct SMSContent
```

## Mentions

- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)

## Topics

### Creating SMS content
- [init(body: String)](smscontent/init(body:).md)
  Initializes a content instance with the given message body.
### Accessing content properties
- [let body: String](smscontent/body.md)
  The body of the SMS message.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let content: SMSContent](smsmessage/content.md)
  The textual content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smscontent)*