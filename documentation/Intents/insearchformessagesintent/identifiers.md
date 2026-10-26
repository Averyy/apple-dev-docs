# identifiers

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The message identifiers to locate in your search.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var identifiers: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * identifiers;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSString *> * identifiers;
```

#### Discussion

When this property contains one or more [`NSString`](../../Foundation/nsstring.md) objects, your search should return only messages whose IDs match the specified identifiers. The value of the [`identifiersOperator`](./identifiersoperator.md) property determines whether searches should be for all, some, or none of the specified identifiers.

## See Also

### Specifying Message Identifiers
- [var identifiersOperator: INConditionalOperator](./identifiersoperator.md)
  The operator that defines how to use the identifiers in the search criteria.
- [var conversationIdentifiers: [String]?](./conversationidentifiers.md)
  The conversation identifiers to locate in your search.
- [var conversationIdentifiersOperator: INConditionalOperator](./conversationidentifiersoperator.md)
  The operator that defines how to use the conversation identifiers in the search criteria.
- [var notificationIdentifiers: [String]?](./notificationidentifiers.md)
  The notification identifiers to locate in your search.
- [var notificationIdentifiersOperator: INConditionalOperator](./notificationidentifiersoperator.md)
  The operator that defines how to use the notification identifiers in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/identifiers)*