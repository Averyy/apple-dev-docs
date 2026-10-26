---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockwatchconnectivitypeer/reply(to:store:sendreply:)"
framework: "CareKit/CareKitStore"
---

# reply(to:store:sendReply:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

You should call this method anytime you receive a message from the companion app. CareKit will inspect the message to see if it contains any synchronization requests that require a response. If there are, the appropriate response will be returned. Be sure to pass the returned keys and values to the reply handler in `WCSessionDelegate`’s `session(_:didReceiveMessage:replyHandler:)` method.

## Declaration

```swift
func reply(to peerMessage: [String : Any], store: OCKStore, sendReply: @escaping (_ message: [String : Any]) -> Void)
```

## Parameters

- `peerMessage`: A message received from the peer for which a response will be created.
- `store`: A store from which the reply can be built.
- `sendReply`: A callback that will be invoked with the response when it is ready.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockwatchconnectivitypeer/reply(to:store:sendreply:))*