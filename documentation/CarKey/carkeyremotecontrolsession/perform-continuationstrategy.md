# perform(_:continuationStrategy:)

**Framework**: CarKey  
**Kind**: method

Sends a request to the vehicle to start an action that has a separate stopping point, and optionally allows your app to have control over incoming continuation requests and to exchange data during the execution of the action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
func perform(_ enduringAction: RemoteKeylessEntryConfigurableEnduringAction, continuationStrategy: CarKeyRemoteControlSession.ContinuationStrategy) throws -> RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest
```

#### Return Value

An object you use to get the results of the initial request and stop the action.

#### Discussion

Call this method for vehicle features that that have both a start and stop point. For example, use it to start raising or lowering the top of a convertible. This method sends the request to the vehicle asynchronously.

Use the returned object to get the execution status of the initial request, and to optionally stop the action.

## Parameters

- `continuationStrategy`: The continuation strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/perform(_:continuationstrategy:))*