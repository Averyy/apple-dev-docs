# CFStreamCreateBoundPair(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a bound pair of read and write streams.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFStreamCreateBoundPair(_ alloc: CFAllocator!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, _ transferBufferSize: CFIndex)
```

#### Discussion

The created streams are bound to one another, such that any data written to `writeStream` is received by `readStream`.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new objects. Pass   or   to use the current default allocator.
- `readStream`: On return, contains a readable stream. Ownership follows the  .
- `writeStream`: On return, contains a writable stream. Ownership follows the  .
- `transferBufferSize`: The size of the buffer, in bytes, used to transfer data from   to  .

## See Also

- [class func getBoundStreams(withBufferSize bufferSize: Int, inputStream: AutoreleasingUnsafeMutablePointer<InputStream?>?, outputStream: AutoreleasingUnsafeMutablePointer<OutputStream?>?)](../Foundation/Stream/getBoundStreams(withBufferSize:inputStream:outputStream:).md)
  Creates and returns by reference a bound pair of input and output streams.
- [func CFStreamCreatePairWithPeerSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithpeersocketsignature(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreatePairWithSocketToHost(CFAllocator!, CFString!, UInt32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsockettohost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a TCP/IP port of a particular host.
- [func CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsocket(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator?, _ host: CFHost, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator?, _ service: CFNetService, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToNetService(_:_:_:_:).md)
  Creates a pair of streams for a CFNetService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamcreateboundpair(_:_:_:_:))*