# CFStreamCreatePairWithPeerSocketSignature(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates readable and writable streams connected to a socket.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

#### Discussion

The streams do not create a socket or connect to the remote host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new objects. Pass   or   to use the current default allocator.
- `signature`: A   structure identifying the communication protocol and address to which the socket streams should connect.
- `readStream`: On return, a readable stream connected to the socket address in  . If you pass  , this function will not create a readable stream. Ownership follows the  .
- `writeStream`: On return, a writable stream connected to the socket address in  . If you pass  , this function will not create a writable stream. Ownership follows the  .

## See Also

- [func CFStreamCreatePairWithSocketToHost(CFAllocator!, CFString!, UInt32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsockettohost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a TCP/IP port of a particular host.
- [func CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsocket(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, CFIndex)](cfstreamcreateboundpair(_:_:_:_:).md)
  Creates a bound pair of read and write streams.
- [func CFStreamCreatePairWithSocketToCFHost(CFAllocator?, CFHost, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(CFAllocator?, CFNetService, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToNetService(_:_:_:_:).md)
  Creates a pair of streams for a CFNetService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithpeersocketsignature(_:_:_:_:))*