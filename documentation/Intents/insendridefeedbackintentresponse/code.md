# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether your app successfully handled the intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var code: INSendRideFeedbackIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSendRideFeedbackIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSendRideFeedbackIntentResponseCode code;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INSendRideFeedbackIntentResponseCode](../insendridefeedbackintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintentresponse/code)*