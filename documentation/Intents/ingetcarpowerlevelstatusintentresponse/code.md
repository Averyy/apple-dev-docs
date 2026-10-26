# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code that indicates success or failure when confirming or handling an intent.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var code: INGetCarPowerLevelStatusIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INGetCarPowerLevelStatusIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INGetCarPowerLevelStatusIntentResponseCode code;
```

#### Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INGetCarPowerLevelStatusIntentResponseCode](../ingetcarpowerlevelstatusintentresponsecode.md)
  Constants that indicate the status of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintentresponse/code)*