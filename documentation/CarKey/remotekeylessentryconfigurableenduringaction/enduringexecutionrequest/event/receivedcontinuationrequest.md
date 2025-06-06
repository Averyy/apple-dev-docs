# RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest.Event.receivedContinuationRequest(_:)

**Framework**: CarKey  
**Kind**: case

Received continuation request from the Vehicle executing the Enduring Action The enduring action may time out on the vehicle side if continuationRequest.continue() or stop() is not invoked promptly upon the receipt of this event.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
case receivedContinuationRequest(RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest.ContinuationRequest)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/event/receivedcontinuationrequest(_:))*