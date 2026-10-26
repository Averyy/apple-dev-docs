# messages

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The array of messages matching the search parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var messages: [INMessage]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INMessage *> * messages;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INMessage *> * messages;
```

#### Discussion

For successful searches, use this property to return messages matching the search parameters. Provide as much information in each [`INMessage`](../inmessage.md) object as you can. Siri may present or read the message details to the user, depending on the messages and how Siri is communicating with the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponse/messages)*