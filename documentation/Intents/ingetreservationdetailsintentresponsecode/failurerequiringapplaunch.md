# INGetReservationDetailsIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to retrieve the reservation details.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INGetReservationDetailsIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you can’t handle the request with Siri for a reason not covered by any other response code. For example, you might use this code if the user hasn’t set up an account with your app. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Request Status
- [INGetReservationDetailsIntentResponseCode.unspecified](./unspecified.md)
  The response code is unspecified.
- [INGetReservationDetailsIntentResponseCode.ready](./ready.md)
  Your app is ready to handle the intent.
- [INGetReservationDetailsIntentResponseCode.inProgress](./inprogress.md)
  Your app is processing the request for reservation details.
- [INGetReservationDetailsIntentResponseCode.success](./success.md)
  Your app successfully handled the intent.
- [INGetReservationDetailsIntentResponseCode.failure](./failure.md)
  Your app is unable to retrieve the reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponsecode/failurerequiringapplaunch)*