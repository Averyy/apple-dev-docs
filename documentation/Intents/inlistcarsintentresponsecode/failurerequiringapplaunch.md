# INListCarsIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates the system must launch your app before you can provide a list of the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INListCarsIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

The system launches the host app when you specify this code. Use this response code when there is a failure that the host app can resolve. Don’t use this code for general errors, or to force a user into the host app even when the extension can handle the intent.

## See Also

### Constants
- [INListCarsIntentResponseCode.failure](./failure.md)
  A response code that indicates you’re unable to retrieve a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.inProgress](./inprogress.md)
  A response code that indicates you’re in the process of retrieving a list of the user’s electric vehicles, but they are not yet available.
- [INListCarsIntentResponseCode.ready](./ready.md)
  A response code that indicates you’re ready to provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.success](./success.md)
  A response code that indicates you’re able to provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates the absence of a genuine response code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponsecode/failurerequiringapplaunch)*