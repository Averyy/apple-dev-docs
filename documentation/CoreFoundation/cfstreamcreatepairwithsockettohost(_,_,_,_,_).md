# CFStreamCreatePairWithSocketToHost(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates readable and writable streams connected to a TCP/IP port of a particular host.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.1+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t in Network framework instead

## Declaration

```swift
func CFStreamCreatePairWithSocketToHost(_ alloc: CFAllocator!, _ host: CFString!, _ port: UInt32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

```c
extern void CFStreamCreatePairWithSocketToHost(CFAllocatorRef alloc, CFStringRef host, UInt32 port, CFReadStreamRef*readStream, CFWriteStreamRef*writeStream);
```

## Discussion

The streams do not create a socket, resolve the hostname, or connect to the remote host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## Parameters

- `alloc`: The allocator to use to allocate memory for the `CFReadStream` and `CFWriteStream` objects. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `host`: The hostname to which the socket streams should connect. The host can be specified using an IPv4 or IPv6 address or a fully qualified DNS hostname.
- `port`: The TCP port number to which the socket streams should connect.
- `readStream`: Upon return, a readable stream connected to the socket address in `port`. If you pass `NULL`, this function will not create a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
- `writeStream`: Upon return, a writable stream connected to the socket address in `port`. If you pass `NULL`, this function will not create a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Streams
- [func CFStreamCreatePairWithPeerSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](./cfstreamcreatepairwithpeersocketsignature%28_,_,_,_%29.md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](./cfstreamcreatepairwithsocket%28_,_,_,_%29.md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, CFIndex)](./cfstreamcreateboundpair%28_,_,_,_%29.md)
  Creates a bound pair of read and write streams.
- [func CFStreamCreatePairWithSocketToCFHost(CFAllocator?, CFHost, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/cfstreamcreatepairwithsockettocfhost%28_,_,_,_,_%29.md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(CFAllocator?, CFNetService, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/cfstreamcreatepairwithsockettonetservice%28_,_,_,_%29.md)
  Creates a pair of streams for a CFNetService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithsockettohost(_:_:_:_:_:))*