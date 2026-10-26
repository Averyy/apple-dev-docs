# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var code: INSendMessageIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSendMessageIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSendMessageIntentResponseCode code;
```

#### Discussion

This property’s value is set at initialization and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INSendMessageIntentResponseCode](../insendmessageintentresponsecode.md)
  Constants that indicate the response state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponse/code)*