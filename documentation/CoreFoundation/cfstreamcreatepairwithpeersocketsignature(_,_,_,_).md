# CFStreamCreatePairWithPeerSocketSignature(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates readable and writable streams connected to a socket.

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
func CFStreamCreatePairWithPeerSocketSignature(_ alloc: CFAllocator!, _ signature: UnsafePointer<CFSocketSignature>!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)
```

```c
extern void CFStreamCreatePairWithPeerSocketSignature(CFAllocatorRef alloc, const CFSocketSignature *signature, CFReadStreamRef*readStream, CFWriteStreamRef*writeStream);
```

## Discussion

The streams do not create a socket or connect to the remote host until you open one of the streams.

Most properties are shared by both streams. Setting a shared property for one stream automatically sets the property for the other.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new objects. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `signature`: A [`CFSocketSignature`](./cfsocketsignature.md) structure identifying the communication protocol and address to which the socket streams should connect.
- `readStream`: On return, a readable stream connected to the socket address in `signature`. If you pass `NULL`, this function will not create a readable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
- `writeStream`: On return, a writable stream connected to the socket address in `signature`. If you pass `NULL`, this function will not create a writable stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Streams
- [func CFStreamCreatePairWithSocketToHost(CFAllocator!, CFString!, UInt32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](./cfstreamcreatepairwithsockettohost%28_,_,_,_,_%29.md)
  Creates readable and writable streams connected to a TCP/IP port of a particular host.
- [func CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](./cfstreamcreatepairwithsocket%28_,_,_,_%29.md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, CFIndex)](./cfstreamcreateboundpair%28_,_,_,_%29.md)
  Creates a bound pair of read and write streams.
- [func CFStreamCreatePairWithSocketToCFHost(CFAllocator?, CFHost, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/cfstreamcreatepairwithsockettocfhost%28_,_,_,_,_%29.md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(CFAllocator?, CFNetService, UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/cfstreamcreatepairwithsockettonetservice%28_,_,_,_%29.md)
  Creates a pair of streams for a CFNetService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamcreatepairwithpeersocketsignature(_:_:_:_:))*