# customIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier that your app uses to identify the person.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var customIdentifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * customIdentifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * customIdentifier;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)
- [Resolving the Parameters of an Intent](../../SiriKit/resolving-the-parameters-of-an-intent.md)

## Discussion

Use this property to access the custom identification string that you specified at initialization time. The value of this property is also returned by the [`vocabularyIdentifier`](../inspeakable/vocabularyidentifier.md) property.

> ❗ **Important**:  The information in this property is for developer purposes only. Use [`personHandle`](./personhandle.md) when your app needs to display identification information to the user.

## See Also

### Accessing app-specific identifiers
- [var contactIdentifier: String?](./contactidentifier.md)
  The Contacts database identifier for the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/customidentifier)*