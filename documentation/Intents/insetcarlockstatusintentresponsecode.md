# INSetCarLockStatusIntentResponseCode

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
enum INSetCarLockStatusIntentResponseCode
```

```c
enum INSetCarLockStatusIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSetCarLockStatusIntentResponseCode.failure](./insetcarlockstatusintentresponsecode/failure.md)
  An error code indicating that you were unable to lock or unlock the car.
- [INSetCarLockStatusIntentResponseCode.failureRequiringAppLaunch](./insetcarlockstatusintentresponsecode/failurerequiringapplaunch.md)
  An error code indicating that the user must launch your app to lock or unlock the car.
- [INSetCarLockStatusIntentResponseCode.inProgress](./insetcarlockstatusintentresponsecode/inprogress.md)
  A response code indicating that your app has attempted to lock or unlock the car, but does not yet have the results.
- [INSetCarLockStatusIntentResponseCode.ready](./insetcarlockstatusintentresponsecode/ready.md)
  A response code indicating that you are ready to handle the intent.
- [INSetCarLockStatusIntentResponseCode.success](./insetcarlockstatusintentresponsecode/success.md)
  A response code indicating that you have successfully handled the intent.
- [INSetCarLockStatusIntentResponseCode.unspecified](./insetcarlockstatusintentresponsecode/unspecified.md)
  A response code indicating that the status was not specified.
### Initializers
- [init?(rawValue: Int)](./insetcarlockstatusintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSetCarLockStatusIntentResponseCode](./insetcarlockstatusintentresponse/code.md)
  The code indicating success or failure when confirming or handling an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintentresponsecode)*