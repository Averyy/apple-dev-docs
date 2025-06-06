# setDataReceiveHandler(_:withContext:)

**Framework**: GameKit  
**Kind**: method

Sets the object that handles data received from other peers connected to the session.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setDataReceiveHandler(_ handler: Any!, withContext context: UnsafeMutableRawPointer!)
```

#### Discussion

The handler must implement a method with the following signature:

```objc
- (void) receiveData:(NSData *)data fromPeer:(NSString *)peer inSession: (GKSession *)session context:(void *)context;
```

where  contains the bytes received from a remote peer,  is a string that identifies the peer,  is the session that received the data, and  is the same context that was passed into the original call to [`setDataReceiveHandler(_:withContext:)`](gksession/setdatareceivehandler(_:withcontext:).md).

> ❗ **Important**:  Data received from other peers should be treated as  data. Be sure to validate the data you receive from the session and write your code carefully to avoid security vulnerabilities. See the [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415) for more information.

 Data received from other peers should be treated as  data. Be sure to validate the data you receive from the session and write your code carefully to avoid security vulnerabilities. See the [`Secure Coding Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415) for more information.

## Parameters

- `handler`: The object you want the session to call when it receives data from other peers.
- `context`: Arbitrary data to be passed to each invocation of the handler.

## See Also

- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](gksession/send(_:topeers:with:).md)
  Transmits a collection of bytes to a list of connected peers.
- [func sendData(toAllPeers: Data!, with: GKSendDataMode) throws](gksession/senddata(toallpeers:with:).md)
  Transmits a collection of bytes to all connected peers.
- [var disconnectTimeout: TimeInterval](gksession/disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](gksession/disconnectfromallpeers.md)
  Disconnects the session from all connected peers.
- [func disconnectPeer(fromAllPeers: String!)](gksession/disconnectpeer(fromallpeers:).md)
  Disconnects a connected peer from all peers connected to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/setdatareceivehandler(_:withcontext:))*