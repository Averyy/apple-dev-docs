# NSXPCCoder

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A coder that encodes and decodes objects that your app sends over an XPC connection.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSXPCCoder
```

```objc
@interface NSXPCCoder : NSCoder
```

## Overview

If you want to perform custom encoding or decoding of [`Codable`](../Swift/codable.md) objects that your app sends over an [`NSXPCConnection`](./nsxpcconnection.md), use [`isKind(of:)`](../ObjectiveC/nsobjectprotocol/iskind%28of%29.md) to determine if the coder provided to your object is a kind of [`NSXPCCoder`](./nsxpccoder.md).

## Topics

### Inspecting the Coder
- [var connection: NSXPCConnection?](./nsxpccoder/connection.md)
  The connection currently performing encoding or decoding.
- [var userInfo: (any NSObjectProtocol)?](./nsxpccoder/userinfo.md)
  An optional user information object associated with the coder.
### Encoding and Decoding
- [func encodeXPCObject(xpc_object_t, forKey: String)](./nsxpccoder/encodexpcobject%28_,forkey%29.md)
  Encodes an object to send over an XPC connection.
- [func decodeXPCObject(ofType: xpc_type_t, forKey: String) -> xpc_object_t?](./nsxpccoder/decodexpcobject%28oftype,forkey%29.md)
  Decodes an object and validates that its type matches the type a service provides over XPC.

## Relationships

### Inherits From
- [NSCoder](./nscoder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### XPC Client
- [protocol NSXPCProxyCreating](./nsxpcproxycreating.md)
  Methods for creating new proxy objects.
- [class NSXPCConnection](./nsxpcconnection.md)
  A bidirectional communication channel between two processes.
- [class NSXPCInterface](./nsxpcinterface.md)
  An interface that may be sent to an exported object or remote object proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpccoder)*