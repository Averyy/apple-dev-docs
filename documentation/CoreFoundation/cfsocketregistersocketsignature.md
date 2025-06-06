# CFSocketRegisterSocketSignature(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Registers a socket signature with a CFSocket name server.

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
func CFSocketRegisterSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafePointer<CFSocketSignature>!) -> CFSocketError
```

#### Return Value

An error code indicating success or failure.

#### Discussion

Once a socket signature is registered, other processes can retrieve it with [`CFSocketCopyRegisteredSocketSignature(_:_:_:_:_:)`](cfsocketcopyregisteredsocketsignature(_:_:_:_:_:).md) and then open a connection to your socket using [`CFSocketCreateConnectedToSocketSignature(_:_:_:_:_:_:)`](cfsocketcreateconnectedtosocketsignature(_:_:_:_:_:_:).md).

To remove a registered socket signature from the name server, use [`CFSocketUnregister(_:_:_:)`](cfsocketunregister(_:_:_:).md).

## Parameters

- `nameServerSignature`: The socket signature for the name server. If  , this function contacts the default server, which is assumed to be a local process using TCP/IP to listen on the port number returned from  . If   is incomplete, the missing values are replaced with the default server’s values, if appropriate.
- `timeout`: The time to wait for the server to accept a connection and to reply to the registration request.
- `name`: The name with which to register  .
- `signature`: The socket signature to register.

## See Also

- [func CFSocketCopyRegisteredSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](cfsocketcopyregisteredsocketsignature(_:_:_:_:_:).md)
  Returns a socket signature registered with a CFSocket name server.
- [func CFSocketCopyRegisteredValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](cfsocketcopyregisteredvalue(_:_:_:_:_:).md)
  Returns a value registered with a CFSocket name server.
- [func CFSocketGetDefaultNameRegistryPortNumber() -> UInt16](cfsocketgetdefaultnameregistryportnumber().md)
  Returns the default port number with which to connect to a CFSocket name server.
- [func CFSocketRegisterValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, CFPropertyList!) -> CFSocketError](cfsocketregistervalue(_:_:_:_:).md)
  Registers a property-list value with a CFSocket name server.
- [func CFSocketSetDefaultNameRegistryPortNumber(UInt16)](cfsocketsetdefaultnameregistryportnumber(_:).md)
  Sets the default port number with which to connect to a CFSocket name server.
- [func CFSocketUnregister(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!) -> CFSocketError](cfsocketunregister(_:_:_:).md)
  Unregisters a value or socket signature with a CFSocket name server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketregistersocketsignature(_:_:_:_:))*