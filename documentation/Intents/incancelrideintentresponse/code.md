# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var code: INCancelRideIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INCancelRideIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INCancelRideIntentResponseCode code;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INCancelRideIntentResponseCode](../incancelrideintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponse/code)*