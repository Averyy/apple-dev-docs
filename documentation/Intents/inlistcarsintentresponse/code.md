# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code that indicates success or failure when confirming or handling the intent.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var code: INListCarsIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INListCarsIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INListCarsIntentResponseCode code;
```

## Discussion

Initializing the response sets the value of this property. You can’t change it.

## See Also

### Getting the Response Code
- [enum INListCarsIntentResponseCode](../inlistcarsintentresponsecode.md)
  Constants that represent the status of a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponse/code)*