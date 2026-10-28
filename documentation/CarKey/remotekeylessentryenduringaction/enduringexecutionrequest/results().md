# results()

**Framework**: CarKey  
**Kind**: method  
**Role**: Instance Method

Returns the results of a preceding action request.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`perform(_:continuationStrategy:)`](../../carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md) instead.

## Declaration

```swift
final func results() async throws -> ExecutionStatus
```

## Return Value

A structure that contains the vehicle-specific status code from the vehicle.

## Discussion

After you call your session’s [`perform(_:)`](../../carkeyremotecontrolsession/perform%28_%29-7mpsy.md) method to send an action request to a vehicle, call this method to await the results of that request. Upon the successful completion of the request, this method returns the vehicle-provided status code. If an error occurs, this method throws the error instead.

## See Also

### Getting the Vehicle’s Response
- [struct ExecutionStatus](../../executionstatus.md)
  A type that contains the status code a vehicle returns after executing an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/enduringexecutionrequest/results())*