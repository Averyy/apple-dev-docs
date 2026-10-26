# INCancelRideIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to cancel the ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case failure
```

```c
INCancelRideIntentResponseCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from canceling the ride. When specifying this code, SiriKit may fall back to other options that include letting the user cancel the ride in your app.

## See Also

### Constants
- [INCancelRideIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INCancelRideIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INCancelRideIntentResponseCode.success](./success.md)
  You successfully canceled the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponsecode/failure)*