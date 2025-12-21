# CFStreamCreatePairWithSocketToHost(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates readable and writable streams connected to a TCP/IP port of a particular host.

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
func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

#### Discussion

The streams do not create a socket, resolve the hostname, or connect to the remote host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## Parameters

- `alloc`: The allocator to use to allocate memory for the   and   objects. Pass   or   to use the current default allocator.
- `host`: The hostname to which the socket streams should connect. The host can be specified using an IPv4 or IPv6 address or a fully qualified DNS hostname.
- `port`: The TCP port number to which the socket streams should connect.
- `readStream`: Upon return, a readable stream connected to the socket address in  . If you pass  , this function will not create a readable stream. Ownership follows the  .
- `writeStream`: Upon return, a writable stream connected to the socket address in  . If you pass  , this function will not create a writable stream. Ownership follows the  .

## See Also

- [func CFStreamCreatePairWithPeerSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithpeersocketsignature(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsocket(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, CFIndex)](cfstreamcreateboundpair(_:_:_:_:).md)
  Creates a bound pair of read and write streams.
- [func CFStreamCreatePairWithSocketToCFHost(CFAllocator?, CFHost, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(CFAllocator?, CFNetService, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToNetService(_:_:_:_:).md)
  Creates a pair of streams for a CFNetService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithsockettohost(_:_:_:_:_:))*