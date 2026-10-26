# speakableGroupNames

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The names of any groups associated with the message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var speakableGroupNames: [INSpeakableString]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INSpeakableString *> * speakableGroupNames;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INSpeakableString *> * speakableGroupNames;
```

#### Discussion

When this property contains one or more strings, your search should return only messages that sent to the specified groups. Use the operator in the [`speakableGroupNamesOperator`](./speakablegroupnamesoperator.md) property to determine whether to search for messages containing all, some, or none of the specified groups.

## See Also

### Getting the Senders and Recipients
- [var recipients: [INPerson]?](./recipients.md)
  The contacts who are the recipients of the messages.
- [var recipientsOperator: INConditionalOperator](./recipientsoperator.md)
  The operator that defines how to use the recipients in the search criteria.
- [var senders: [INPerson]?](./senders.md)
  The senders to include or exclude when you search for messages.
- [var sendersOperator: INConditionalOperator](./sendersoperator.md)
  The operator that defines how to use the senders in the search criteria.
- [var speakableGroupNamesOperator: INConditionalOperator](./speakablegroupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/speakablegroupnames)*