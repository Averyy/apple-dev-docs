# siriMatches

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The list of matches Siri provides for you to resolve or disambiguate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var siriMatches: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * siriMatches;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * siriMatches;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Discussion

When attempting to resolve the recipient of a message, use this property to determine how to respond:

- If the array contains a single match and your app successfully identifies that person by their [`contactIdentifier`](./contactidentifier.md) or [`customIdentifier`](./customidentifier.md), use the [`success(with:)`](../inpersonresolutionresult/success%28with%29.md) method to resolve the recipient.
- If the array contains multiple people and those people each have distinct [`contactIdentifier`](./contactidentifier.md) or [`customIdentifier`](./customidentifier.md) values, ignore any your app can’t identify and then respond according to the number of remaining matches. For example, if there are still two or more matches, use the [`disambiguation(with:)`](../inpersonresolutionresult/disambiguation%28with%29.md) method to ask the person interacting with Siri to choose.
- If the array contains multiple people and they all have the same [`contactIdentifier`](./contactidentifier.md), disambiguate using [`personHandle`](./personhandle.md) instead. If your app doesn’t use handles, simply pass any match to the [`success(with:)`](../inpersonresolutionresult/success%28with%29.md) method.
- If the array is empty or the property is `nil`, search your app’s contacts for people matching those in the [`recipients`](../insendmessageintent/recipients.md) property of [`INSendMessageIntent`](../insendmessageintent.md) instead. Use the resolution method that best describes the outcome of that search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/sirimatches)*