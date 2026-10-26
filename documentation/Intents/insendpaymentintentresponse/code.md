# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var code: INSendPaymentIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSendPaymentIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSendPaymentIntentResponseCode code;
```

#### Discussion

The value of this property is set automatically at initialization time and cant be changed later.

## See Also

### Getting the Response Code
- [enum INSendPaymentIntentResponseCode](../insendpaymentintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendpaymentintentresponse/code)*