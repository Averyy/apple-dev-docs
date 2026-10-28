# INListCarsIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates you’re in the process of retrieving a list of the user’s electric vehicles, but they are not yet available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
case inProgress
```

```c
INListCarsIntentResponseCodeInProgress
```

## Discussion

Use this code during the handling phase of intent handling if the request is likely to take more than a few seconds to complete.

## See Also

### Constants
- [INListCarsIntentResponseCode.failure](./failure.md)
  A response code that indicates you’re unable to retrieve a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the system must launch your app before you can provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.ready](./ready.md)
  A response code that indicates you’re ready to provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.success](./success.md)
  A response code that indicates you’re able to provide a list of the user’s electric vehicles.
- [INListCarsIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates the absence of a genuine response code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponsecode/inprogress)*