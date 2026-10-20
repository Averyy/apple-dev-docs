# sendData(toAllPeers:with:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Transmits a collection of bytes to all connected peers.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported.

## Declaration

```swift
func sendData(toAllPeers data: Data!, with mode: GKSendDataMode) throws
```

```objc
- (BOOL) sendDataToAllPeers:(NSData *) data withDataMode:(GKSendDataMode) mode error:(NSError **) error;
```

#### Discussion

The session queues the data and transmits it when the network is free.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: The bytes to be sent.
- `mode`: The mechanism used to send the data.

## See Also

### Working with Connected Peers
- [func setDataReceiveHandler(Any!, withContext: UnsafeMutableRawPointer!)](./setdatareceivehandler%28_,withcontext%29.md)
  Sets the object that handles data received from other peers connected to the session.
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](./send%28_,topeers,with%29.md)
  Transmits a collection of bytes to a list of connected peers.
- [var disconnectTimeout: TimeInterval](./disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](./disconnectfromallpeers%28%29.md)
  Disconnects the session from all connected peers.
- [func disconnectPeer(fromAllPeers: String!)](./disconnectpeer%28fromallpeers%29.md)
  Disconnects a connected peer from all peers connected to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/senddata(toallpeers:with:))*