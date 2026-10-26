# INGetReservationDetailsIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the status of the request for reservations details.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INGetReservationDetailsIntentResponseCode
```

```c
enum INGetReservationDetailsIntentResponseCode : NSInteger;
```

## Topics

### Request Status
- [INGetReservationDetailsIntentResponseCode.unspecified](./ingetreservationdetailsintentresponsecode/unspecified.md)
  The response code is unspecified.
- [INGetReservationDetailsIntentResponseCode.ready](./ingetreservationdetailsintentresponsecode/ready.md)
  Your app is ready to handle the intent.
- [INGetReservationDetailsIntentResponseCode.inProgress](./ingetreservationdetailsintentresponsecode/inprogress.md)
  Your app is processing the request for reservation details.
- [INGetReservationDetailsIntentResponseCode.success](./ingetreservationdetailsintentresponsecode/success.md)
  Your app successfully handled the intent.
- [INGetReservationDetailsIntentResponseCode.failure](./ingetreservationdetailsintentresponsecode/failure.md)
  Your app is unable to retrieve the reservation details.
- [INGetReservationDetailsIntentResponseCode.failureRequiringAppLaunch](./ingetreservationdetailsintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to retrieve the reservation details.
### Initializers
- [init?(rawValue: Int)](./ingetreservationdetailsintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INGetReservationDetailsIntentResponseCode](./ingetreservationdetailsintentresponse/code.md)
  The code that indicates whether your app successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponsecode)*