# CFStream

**Framework**: Core Foundation

#### Overview

This document describes the generic `CFStream` functions, data types, and constants. See also [`CFReadStream`](cfreadstream.md) and [`CFWriteStream`](cfwritestream.md) for functions and constants specific to read and write streams respectively.

> **Note**:  When you use the `CFStream` API for networking, read and write operations on sockets can block. To prevent blocking: 1. Call [`CFReadStreamSetClient(_:_:_:_:)`](cfreadstreamsetclient(_:_:_:_:).md) and [`CFWriteStreamSetClient(_:_:_:_:)`](cfwritestreamsetclient(_:_:_:_:).md) to register to receive stream-related event notifications.
2. Call [`CFReadStreamScheduleWithRunLoop(_:_:_:)`](cfreadstreamschedulewithrunloop(_:_:_:).md) and [`CFWriteStreamScheduleWithRunLoop(_:_:_:)`](cfwritestreamschedulewithrunloop(_:_:_:).md) to schedule the stream on a run loop for receiving stream-related event notifications.
3. Call [`CFReadStreamOpen(_:)`](cfreadstreamopen(_:).md) and [`CFWriteStreamOpen(_:)`](cfwritestreamopen(_:).md) to open each stream.
4. Read only after receiving a [`hasBytesAvailable`](cfstreameventtype/hasbytesavailable.md) notification. Write only after receiving a [`canAcceptBytes`](cfstreameventtype/canacceptbytes.md) notification.

## Topics

### Creating Streams
- [func CFStreamCreatePairWithPeerSocketSignature(CFAllocator!, UnsafePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithpeersocketsignature(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreatePairWithSocketToHost(CFAllocator!, CFString!, UInt32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsockettohost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a TCP/IP port of a particular host.
- [func CFStreamCreatePairWithSocket(CFAllocator!, CFSocketNativeHandle, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!)](cfstreamcreatepairwithsocket(_:_:_:_:).md)
  Creates readable and writable streams connected to a socket.
- [func CFStreamCreateBoundPair(CFAllocator!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>!, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>!, CFIndex)](cfstreamcreateboundpair(_:_:_:_:).md)
  Creates a bound pair of read and write streams.
- [func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator?, _ host: CFHost, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToCFHost(_:_:_:_:_:).md)
  Creates readable and writable streams connected to a given `CFHost` object.
- [func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator?, _ service: CFNetService, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>?, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>?)](../CFNetwork/CFStreamCreatePairWithSocketToNetService(_:_:_:_:).md)
  Creates a pair of streams for a CFNetService.
### Obtaining Errors
- [func CFSocketStreamSOCKSGetError(_ error: UnsafePointer<CFStreamError>) -> Int32](../CFNetwork/CFSocketStreamSOCKSGetError(_:).md)
  This function gets error codes in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.
- [func CFSocketStreamSOCKSGetErrorSubdomain(_ error: UnsafePointer<CFStreamError>) -> Int32](../CFNetwork/CFSocketStreamSOCKSGetErrorSubdomain(_:).md)
  Gets the error subdomain associated with errors in the `kCFStreamErrorDomainSOCKS` domain from the `CFStreamError` returned by a stream operation.
### Setting the Security Protocol
- [func CFReadStreamSetProperty(CFReadStream!, CFStreamPropertyKey!, CFTypeRef!) -> Bool](cfreadstreamsetproperty(_:_:_:).md)
  Sets the value of a property for a stream.
- [func CFWriteStreamSetProperty(CFWriteStream!, CFStreamPropertyKey!, CFTypeRef!) -> Bool](cfwritestreamsetproperty(_:_:_:).md)
  Sets the value of a property for a stream.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
### Data Types
- [struct CFStreamError](cfstreamerror.md)
  The structure returned by [`CFReadStreamGetError(_:)`](cfreadstreamgeterror(_:).md) and [`CFWriteStreamGetError(_:)`](cfwritestreamgeterror(_:).md).
- [struct CFStreamClientContext](cfstreamclientcontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.
### Constants
- [enum CFStreamStatus](cfstreamstatus.md)
  Constants that describe the status of a stream.
- [enum CFStreamErrorDomain](cfstreamerrordomain.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md)
  Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../CFNetwork/1518266-secure-sockets-socks-errors.md)
  Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [struct CFStreamEventType](cfstreameventtype.md)
  Defines constants for stream-related events.
- [Stream Properties](stream-properties.md)
  Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md)
  Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md)
  Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md)
  String constants that specify the service type of a stream.

## See Also

- [Getting Started with Networking, Internet, and Web](https://developer.apple.comhttps://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_NetworkingInternetWeb/_index.html#//apple_ref/doc/uid/TP40008807)
- [CFNetwork Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001132)
- [Core Foundation Structures](core-foundation-structures.md)
- [Core Foundation Enumerations](core-foundation-enumerations.md)
- [Core Foundation Constants](core-foundation-constants.md)
- [Core Foundation Functions](core-foundation-functions.md)
- [Core Foundation Data Types](core-foundation-data-types.md)
- [Core Foundation Macros](corefoundation-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstream)*