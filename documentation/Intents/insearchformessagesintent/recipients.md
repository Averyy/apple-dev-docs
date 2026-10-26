# recipients

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The contacts who are the recipients of the messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var recipients: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * recipients;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * recipients;
```

#### Discussion

When this property contains one or more [`INPerson`](../inperson.md) objects, your search should return only messages received by the specified users. Use the operator in the [`recipientsOperator`](./recipientsoperator.md) property to determine whether to search for messages containing all, some, or none of the specified recipients.

## See Also

### Getting the Senders and Recipients
- [var recipientsOperator: INConditionalOperator](./recipientsoperator.md)
  The operator that defines how to use the recipients in the search criteria.
- [var senders: [INPerson]?](./senders.md)
  The senders to include or exclude when you search for messages.
- [var sendersOperator: INConditionalOperator](./sendersoperator.md)
  The operator that defines how to use the senders in the search criteria.
- [var speakableGroupNames: [INSpeakableString]?](./speakablegroupnames.md)
  The names of any groups associated with the message.
- [var speakableGroupNamesOperator: INConditionalOperator](./speakablegroupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/recipients)*