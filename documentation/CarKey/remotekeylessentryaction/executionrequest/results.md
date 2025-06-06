# results()

**Framework**: CarKey  
**Kind**: method

Returns the results of a preceding action request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
final func results() async throws -> ExecutionStatus
```

#### Return Value

A structure that contains the vehicle-specific status code from the vehicle.

#### Discussion

After you call your session’s [`perform(_:)`](carkeyremotecontrolsession/perform(_:)-8ac0c.md) method to send an action request to a vehicle, call this method and await the results of that request. Upon the successful completion of the request, this method returns the vehicle-provided status code. If an error occurs, this method throws the error instead.

## See Also

- [struct ExecutionStatus](executionstatus.md)
  A type that contains the status code a vehicle returns after executing an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryaction/executionrequest/results())*