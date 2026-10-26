# conversationIdentifiers

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The conversation identifiers to locate in your search.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var conversationIdentifiers: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * conversationIdentifiers;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSString *> * conversationIdentifiers;
```

#### Discussion

When this property contains one or more strings, your search should return only messages with conversation IDs matching the specified identifiers. The value of the [`conversationIdentifiersOperator`](./conversationidentifiersoperator.md) property determines whether searches should be for all, some, or none of the specified conversation identifiers.

## See Also

### Specifying Message Identifiers
- [var identifiers: [String]?](./identifiers.md)
  The message identifiers to locate in your search.
- [var identifiersOperator: INConditionalOperator](./identifiersoperator.md)
  The operator that defines how to use the identifiers in the search criteria.
- [var conversationIdentifiersOperator: INConditionalOperator](./conversationidentifiersoperator.md)
  The operator that defines how to use the conversation identifiers in the search criteria.
- [var notificationIdentifiers: [String]?](./notificationidentifiers.md)
  The notification identifiers to locate in your search.
- [var notificationIdentifiersOperator: INConditionalOperator](./notificationidentifiersoperator.md)
  The operator that defines how to use the notification identifiers in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/conversationidentifiers)*