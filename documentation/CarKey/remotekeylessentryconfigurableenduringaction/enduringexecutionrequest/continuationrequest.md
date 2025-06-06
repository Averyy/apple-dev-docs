# RemoteKeylessEntryConfigurableEnduringAction.EnduringExecutionRequest.ContinuationRequest

**Framework**: CarKey  
**Kind**: struct

Continuation Request

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
struct ContinuationRequest
```

## Topics

### Instance Properties
- [let data: Data?](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/continuationrequest/data.md)
  Optional data sent from the vehicle along with this continuation request. Max 64 bytes
### Instance Methods
- [func confirm(Data?) throws](remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/continuationrequest/confirm(_:).md)
  Method for your app to acknowledge receipt of this continuation request and commit to continue execution of this enduring action with optional arbitrary data to send to the vehicle. There is a maximum length of 64 bytes for the data to be sent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryconfigurableenduringaction/enduringexecutionrequest/continuationrequest)*