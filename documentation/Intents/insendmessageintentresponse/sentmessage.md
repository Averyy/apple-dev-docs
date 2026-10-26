# sentMessage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The message sent by the intent.

**Availability**:
- iOS 10.3+ - Deprecated in 16.0
- iPadOS 10.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 9.0

## Declaration

```swift
@NSCopying
var sentMessage: INMessage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INMessage * sentMessage;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INMessage * sentMessage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponse/sentmessage)*