# SMSContent

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that holds the content of an SMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct SMSContent
```

## Mentions

- [Creating a carrier messaging app](./creating-a-carrier-messaging-app.md)

## Topics

### Creating SMS content
- [init(body: String)](./smscontent/init%28body%29.md)
  Initializes a content instance with the given message body.
### Accessing content properties
- [let body: String](./smscontent/body.md)
  The body of the SMS message.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing message content
- [let content: SMSContent](./smsmessage/content.md)
  The textual content of the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smscontent)*