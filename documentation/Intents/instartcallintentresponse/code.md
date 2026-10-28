# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var code: INStartCallIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INStartCallIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INStartCallIntentResponseCode code;
```

## Discussion

This property’s value is set automatically at initialization and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INStartCallIntentResponseCode](../instartcallintentresponsecode.md)
  Constants that indicate the response state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintentresponse/code)*