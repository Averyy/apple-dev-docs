# speakableGroupNamesOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to use the group names in the search criteria.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var speakableGroupNamesOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator speakableGroupNamesOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator speakableGroupNamesOperator;
```

## Discussion

This property indicates whether the message must contain all, some, or none of the groups listed in the [`speakableGroupNames`](./speakablegroupnames.md) property.

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
- [var speakableGroupNames: [INSpeakableString]?](./speakablegroupnames.md)
  The names of any groups associated with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/speakablegroupnamesoperator)*