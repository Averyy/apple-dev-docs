# INCancelRideIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum INCancelRideIntentResponseCode
```

```c
enum INCancelRideIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INCancelRideIntentResponseCode.unspecified](./incancelrideintentresponsecode/unspecified.md)
  There is no specified response code.
- [INCancelRideIntentResponseCode.ready](./incancelrideintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INCancelRideIntentResponseCode.success](./incancelrideintentresponsecode/success.md)
  You successfully canceled the ride.
- [INCancelRideIntentResponseCode.failure](./incancelrideintentresponsecode/failure.md)
  You were unable to cancel the ride.
### Initializers
- [init?(rawValue: Int)](./incancelrideintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INCancelRideIntentResponseCode](./incancelrideintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponsecode)*