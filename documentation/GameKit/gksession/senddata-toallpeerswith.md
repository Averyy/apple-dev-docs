# sendData(toAllPeers:with:)

**Framework**: GameKit  
**Kind**: method

Transmits a collection of bytes to all connected peers.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func sendData(toAllPeers data: Data!, with mode: GKSendDataMode) throws
```

#### Discussion

The session queues the data and transmits it when the network is free.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: The bytes to be sent.
- `mode`: The mechanism used to send the data.

## See Also

- [func setDataReceiveHandler(Any!, withContext: UnsafeMutableRawPointer!)](gksession/setdatareceivehandler(_:withcontext:).md)
  Sets the object that handles data received from other peers connected to the session.
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](gksession/send(_:topeers:with:).md)
  Transmits a collection of bytes to a list of connected peers.
- [var disconnectTimeout: TimeInterval](gksession/disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](gksession/disconnectfromallpeers.md)
  Disconnects the session from all connected peers.
- [func disconnectPeer(fromAllPeers: String!)](gksession/disconnectpeer(fromallpeers:).md)
  Disconnects a connected peer from all peers connected to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/senddata(toallpeers:with:))*