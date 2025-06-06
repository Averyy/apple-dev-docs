# results()

**Framework**: CarKey  
**Kind**: method

Returns the results of a preceding action request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
final func results() async throws -> ExecutionStatus
```

#### Return Value

A structure that contains the vehicle-specific status code from the vehicle.

#### Discussion

After you call your session’s [`perform(_:)`](carkeyremotecontrolsession/perform(_:)-7mpsy.md) method to send an action request to a vehicle, call this method to await the results of that request. Upon the successful completion of the request, this method returns the vehicle-provided status code. If an error occurs, this method throws the error instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/results())*