# conversationIdentifiersOperator

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator that defines how to use the conversation identifiers in the search criteria.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var conversationIdentifiersOperator: INConditionalOperator { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INConditionalOperator conversationIdentifiersOperator;
```

*macOS*

```objc
@property (atomic, assign, readonly) INConditionalOperator conversationIdentifiersOperator;
```

#### Discussion

This property indicates whether the message must contain all, some, or none of the conversation identifiers listed in the [`conversationIdentifiers`](./conversationidentifiers.md) property.

## See Also

### Specifying Message Identifiers
- [var identifiers: [String]?](./identifiers.md)
  The message identifiers to locate in your search.
- [var identifiersOperator: INConditionalOperator](./identifiersoperator.md)
  The operator that defines how to use the identifiers in the search criteria.
- [var conversationIdentifiers: [String]?](./conversationidentifiers.md)
  The conversation identifiers to locate in your search.
- [var notificationIdentifiers: [String]?](./notificationidentifiers.md)
  The notification identifiers to locate in your search.
- [var notificationIdentifiersOperator: INConditionalOperator](./notificationidentifiersoperator.md)
  The operator that defines how to use the notification identifiers in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/conversationidentifiersoperator)*