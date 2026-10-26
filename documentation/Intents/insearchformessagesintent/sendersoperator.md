# sendersOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to use the senders in the search criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var sendersOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator sendersOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator sendersOperator;
```

#### Discussion

This property indicates whether the message must contain (or not contain) one of the people listed in the [`senders`](./senders.md) property.

## See Also

### Getting the Senders and Recipients
- [var recipients: [INPerson]?](./recipients.md)
  The contacts who are the recipients of the messages.
- [var recipientsOperator: INConditionalOperator](./recipientsoperator.md)
  The operator that defines how to use the recipients in the search criteria.
- [var senders: [INPerson]?](./senders.md)
  The senders to include or exclude when you search for messages.
- [var speakableGroupNames: [INSpeakableString]?](./speakablegroupnames.md)
  The names of any groups associated with the message.
- [var speakableGroupNamesOperator: INConditionalOperator](./speakablegroupnamesoperator.md)
  The operator that defines how to use the group names in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/sendersoperator)*