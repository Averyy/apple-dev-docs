# INGetReservationDetailsIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your app successfully handled the intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case success
```

```c
INGetReservationDetailsIntentResponseCodeSuccess
```

#### Discussion

Use this code when your app has successfully retrieved the reservation details.

## See Also

### Request Status
- [INGetReservationDetailsIntentResponseCode.unspecified](./unspecified.md)
  The response code is unspecified.
- [INGetReservationDetailsIntentResponseCode.ready](./ready.md)
  Your app is ready to handle the intent.
- [INGetReservationDetailsIntentResponseCode.inProgress](./inprogress.md)
  Your app is processing the request for reservation details.
- [INGetReservationDetailsIntentResponseCode.failure](./failure.md)
  Your app is unable to retrieve the reservation details.
- [INGetReservationDetailsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to retrieve the reservation details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponsecode/success)*