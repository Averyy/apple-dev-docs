# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether your app successfully handled the intent.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var code: INCreateTaskListIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INCreateTaskListIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INCreateTaskListIntentResponseCode code;
```

## See Also

### Getting the Response Code
- [enum INCreateTaskListIntentResponseCode](../increatetasklistintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponse/code)*