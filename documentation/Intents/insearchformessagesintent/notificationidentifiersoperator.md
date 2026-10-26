# notificationIdentifiersOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to use the notification identifiers in the search criteria.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var notificationIdentifiersOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator notificationIdentifiersOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator notificationIdentifiersOperator;
```

#### Discussion

This property indicates whether the message must contain all, some, or none of the identifiers in the [`notificationIdentifiers`](./notificationidentifiers.md) property.

## See Also

### Specifying Message Identifiers
- [var identifiers: [String]?](./identifiers.md)
  The message identifiers to locate in your search.
- [var identifiersOperator: INConditionalOperator](./identifiersoperator.md)
  The operator that defines how to use the identifiers in the search criteria.
- [var conversationIdentifiers: [String]?](./conversationidentifiers.md)
  The conversation identifiers to locate in your search.
- [var conversationIdentifiersOperator: INConditionalOperator](./conversationidentifiersoperator.md)
  The operator that defines how to use the conversation identifiers in the search criteria.
- [var notificationIdentifiers: [String]?](./notificationidentifiers.md)
  The notification identifiers to locate in your search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/notificationidentifiersoperator)*