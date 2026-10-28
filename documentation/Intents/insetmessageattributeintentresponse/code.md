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

## Declaration

```swift
var code: INSetMessageAttributeIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSetMessageAttributeIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSetMessageAttributeIntentResponseCode code;
```

## Discussion

This property’s value is set automatically at initialization and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INSetMessageAttributeIntentResponseCode](../insetmessageattributeintentresponsecode.md)
  Constants that indicate the response state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponse/code)*