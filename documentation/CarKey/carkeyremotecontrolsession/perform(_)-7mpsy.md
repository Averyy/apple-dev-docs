# perform(_:)

**Framework**: CarKey  
**Kind**: method  
**Role**: Instance Method

Sends a request to the vehicle to start an action that has a separate stopping point.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use perform(enduringAction:continuationStrategy:) instead

## Declaration

```swift
func perform(_ enduringAction: RemoteKeylessEntryEnduringAction) throws -> RemoteKeylessEntryEnduringAction.EnduringExecutionRequest
```

## Return Value

An object you use to get the results of the initial request and stop the action.

## Discussion

Call this method for vehicle features that that have both a start and stop point. For example, use it to start raising or lowering the top of a convertible. This method sends the request to the vehicle asynchronously.

Use the returned object to get the execution status of the initial request, and to optionally stop the action.

## See Also

### Performing Vehicle-Related Actions
- [func perform(RemoteKeylessEntryAction) throws -> RemoteKeylessEntryAction.ExecutionRequest](./perform%28_%29-8ac0c.md)
  Sends a request to the vehicle to perform a one-time action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/perform(_:)-7mpsy)*