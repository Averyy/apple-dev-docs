# setDataReceiveHandler(_:withContext:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sets the object that handles data received from other peers connected to the session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func setDataReceiveHandler(_ handler: Any!, withContext context: UnsafeMutableRawPointer!)
```

```objc
- (void) setDataReceiveHandler:(id) handler withContext:(void *) context;
```

## Discussion

The handler must implement a method with the following signature:

```objc
- (void) receiveData:(NSData *)data fromPeer:(NSString *)peer inSession: (GKSession *)session context:(void *)context;
```

where *data* contains the bytes received from a remote peer, *peer* is a string that identifies the peer, *session* is the session that received the data, and *context* is the same context that was passed into the original call to [`setDataReceiveHandler(_:withContext:)`](./setdatareceivehandler%28_,withcontext%29.md).

> ❗ **Important**:  Data received from other peers should be treated as *untrusted* data. Be sure to validate the data you receive from the session and write your code carefully to avoid security vulnerabilities. See the [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415) for more information.

## Parameters

- `handler`: The object you want the session to call when it receives data from other peers.
- `context`: Arbitrary data to be passed to each invocation of the handler.

## See Also

### Working with Connected Peers
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](./send%28_,topeers,with%29.md)
  Transmits a collection of bytes to a list of connected peers.
- [func sendData(toAllPeers: Data!, with: GKSendDataMode) throws](./senddata%28toallpeers,with%29.md)
  Transmits a collection of bytes to all connected peers.
- [var disconnectTimeout: TimeInterval](./disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](./disconnectfromallpeers%28%29.md)
  Disconnects the session from all connected peers.
- [func disconnectPeer(fromAllPeers: String!)](./disconnectpeer%28fromallpeers%29.md)
  Disconnects a connected peer from all peers connected to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/setdatareceivehandler(_:withcontext:))*