# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
var code: INStartVideoCallIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INStartVideoCallIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INStartVideoCallIntentResponseCode code;
```

## See Also

### Getting the Response Code
- [enum INStartVideoCallIntentResponseCode](../instartvideocallintentresponsecode.md)
  Constants indicating the status of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintentresponse/code)*