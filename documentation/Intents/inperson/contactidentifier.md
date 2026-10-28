# contactIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The Contacts database identifier for the person.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var contactIdentifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * contactIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * contactIdentifier;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Discussion

> ❗ **Important**:  When donating instances of [`INSendMessageIntent`](../insendmessageintent.md), specify a value for this property for each recipient. This enables Siri to choose and interact with the appropriate messaging app when a person asks to send a message.

If your app doesn’t have permission to access the Contacts database, this property returns `nil`. Otherwise, it returns the value you specify when creating the person.

## See Also

### Accessing app-specific identifiers
- [var customIdentifier: String?](./customidentifier.md)
  The unique identifier that your app uses to identify the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/contactidentifier)*