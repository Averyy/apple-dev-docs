# notificationIdentifiers

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The notification identifiers to locate in your search.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var notificationIdentifiers: [String]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * notificationIdentifiers;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<NSString *> * notificationIdentifiers;
```

#### Discussion

When this property contains one or more [`NSString`](../../Foundation/nsstring.md) objects, your search should return [`UNNotification`](../../UserNotifications/unnotification.md) objects whose IDs match the specified strings. The [`UNNotificationRequest`](../../UserNotifications/unnotificationrequest.md) object, which is part of the notification, stores the notification’s identifier. You can use these identifiers to search your app’s delivered local and remote notifications.

The value of the [`notificationIdentifiersOperator`](./notificationidentifiersoperator.md) property determines whether searches should be for all, some, or none of the specified notification identifiers.

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
- [var notificationIdentifiersOperator: INConditionalOperator](./notificationidentifiersoperator.md)
  The operator that defines how to use the notification identifiers in the search criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintent/notificationidentifiers)*