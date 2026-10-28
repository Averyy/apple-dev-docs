# INGetReservationDetailsIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your app is ready to handle the intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case ready
```

```c
INGetReservationDetailsIntentResponseCodeReady
```

## Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Request Status
- [INGetReservationDetailsIntentResponseCode.unspecified](./unspecified.md)
  The response code is unspecified.
- [INGetReservationDetailsIntentResponseCode.inProgress](./inprogress.md)
  Your app is processing the request for reservation details.
- [INGetReservationDetailsIntentResponseCode.success](./success.md)
  Your app successfully handled the intent.
- [INGetReservationDetailsIntentResponseCode.failure](./failure.md)
  Your app is unable to retrieve the reservation details.
- [INGetReservationDetailsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to retrieve the reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponsecode/ready)*