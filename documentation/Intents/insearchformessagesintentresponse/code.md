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
var code: INSearchForMessagesIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSearchForMessagesIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSearchForMessagesIntentResponseCode code;
```

#### Discussion

This propertyue’s val is set at initialization and it can’t be changed later.

## See Also

### Getting the Response Code
- [enum INSearchForMessagesIntentResponseCode](../insearchformessagesintentresponsecode.md)
  Constants that indicate the response state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformessagesintentresponse/code)*