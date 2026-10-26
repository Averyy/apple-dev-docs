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
- watchOS 3.2+ - Deprecated in 6.0

> **Deprecated**: INStartAudioCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
var code: INStartAudioCallIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INStartAudioCallIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INStartAudioCallIntentResponseCode code;
```

## See Also

### Getting the Response Code
- [enum INStartAudioCallIntentResponseCode](../instartaudiocallintentresponsecode.md)
  Constants indicating the status of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintentresponse/code)*