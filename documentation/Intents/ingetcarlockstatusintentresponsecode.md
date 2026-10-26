# INGetCarLockStatusIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INGetCarLockStatusIntentResponseCode
```

```c
enum INGetCarLockStatusIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INGetCarLockStatusIntentResponseCode.failure](./ingetcarlockstatusintentresponsecode/failure.md)
  An error code indicating that you were unable to get the car’s lock status.
- [INGetCarLockStatusIntentResponseCode.failureRequiringAppLaunch](./ingetcarlockstatusintentresponsecode/failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to get the car’s lock status.
- [INGetCarLockStatusIntentResponseCode.inProgress](./ingetcarlockstatusintentresponsecode/inprogress.md)
  A response code indicating that you are getting the car’s lock status but do not yet have the results.
- [INGetCarLockStatusIntentResponseCode.ready](./ingetcarlockstatusintentresponsecode/ready.md)
  A response code indicating that you are ready to handle the intent.
- [INGetCarLockStatusIntentResponseCode.success](./ingetcarlockstatusintentresponsecode/success.md)
  A response code indicating that you have successfully handled the intent.
- [INGetCarLockStatusIntentResponseCode.unspecified](./ingetcarlockstatusintentresponsecode/unspecified.md)
  A response code indicating that the status was not specified.
### Initializers
- [init?(rawValue: Int)](./ingetcarlockstatusintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INGetCarLockStatusIntentResponseCode](./ingetcarlockstatusintentresponse/code.md)
  The code indicating success or failure when confirming or handling an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintentresponsecode)*