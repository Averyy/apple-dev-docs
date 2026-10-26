# INCancelRideIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully canceled the ride.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case success
```

```c
INCancelRideIntentResponseCodeSuccess
```

#### Discussion

Use this code during the handling phase to indicate that your ride service acknowledged the cancellation of the ride. You can also specify this code during the confirmation phase to indicate that you are ready to handle the intent.

## See Also

### Constants
- [INCancelRideIntentResponseCode.unspecified](./unspecified.md)
  There is no specified response code.
- [INCancelRideIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INCancelRideIntentResponseCode.failure](./failure.md)
  You were unable to cancel the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponsecode/success)*