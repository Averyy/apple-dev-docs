# senders

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The senders to include or exclude when you search for messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var senders: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * senders;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * senders;
```

## Discussion

When this property contains one or more [`INPerson`](../inperson.md) objects, your search should return only messages sent by the specified users. Use the [`sendersOperator`](./sendersoperator.md) property to determine whether to search for messages sent by any of the users, or not sent by any of the users.

## See Also

### Getting the Senders and Recipients
- [var recipients: [INPerson]?](./recipients.md)
  The contacts who are the recipients of the messages.
- [var recipientsOperator: INConditionalOperator](./recipientsoperator.md)
  The operator that defines how to use the recipients in the search criteria.
- [var sendersOperator: INConditionalOperator](./sendersoperator.md)
  The operator that defines how to use the senders in the search criteria.
- [var speakableGroupNames: [INSpeakableString]?](./speakablegroupnames.md)
  The names of any groups associated with the message.
- [var speakableGroupNamesOperator: INConditionalOperator](./speakablegroupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/senders)*