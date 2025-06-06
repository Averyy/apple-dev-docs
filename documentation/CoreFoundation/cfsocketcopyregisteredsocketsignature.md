# CFSocketCopyRegisteredSocketSignature(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a socket signature registered with a CFSocket name server.

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
func CFSocketCopyRegisteredSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafeMutablePointer<CFSocketSignature>!, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError
```

#### Return Value

An error code indicating success or failure.

#### Discussion

Once you have the socket signature, you can open a connection to that socket with [`CFSocketCreateConnectedToSocketSignature(_:_:_:_:_:_:)`](cfsocketcreateconnectedtosocketsignature(_:_:_:_:_:_:).md).

## Parameters

- `nameServerSignature`: The socket signature for the name server. If  , this function contacts the default server, which is assumed to be a local process using TCP/IP to listen on the port number returned from  . If   is incomplete, the missing values are replaced with the default server’s values, if appropriate.
- `timeout`: The time to wait for the server to accept a connection and to reply to the registration request.
- `name`: The name of the registered socket signature to retrieve.
- `signature`: A pointer to a   structure into which the retrieved socket signature is copied.
- `nameServerAddress`: A pointer to a CFData object into which the name server’s address is copied. Pass   if you do not want the server’s address.

## See Also

- [func CFSocketCopyRegisteredValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](cfsocketcopyregisteredvalue(_:_:_:_:_:).md)
  Returns a value registered with a CFSocket name server.
- [func CFSocketGetDefaultNameRegistryPortNumber() -> UInt16](cfsocketgetdefaultnameregistryportnumber().md)
  Returns the default port number with which to connect to a CFSocket name server.
- [func CFSocketRegisterSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafePointer<CFSocketSignature>!) -> CFSocketError](cfsocketregistersocketsignature(_:_:_:_:).md)
  Registers a socket signature with a CFSocket name server.
- [func CFSocketRegisterValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, CFPropertyList!) -> CFSocketError](cfsocketregistervalue(_:_:_:_:).md)
  Registers a property-list value with a CFSocket name server.
- [func CFSocketSetDefaultNameRegistryPortNumber(UInt16)](cfsocketsetdefaultnameregistryportnumber(_:).md)
  Sets the default port number with which to connect to a CFSocket name server.
- [func CFSocketUnregister(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!) -> CFSocketError](cfsocketunregister(_:_:_:).md)
  Unregisters a value or socket signature with a CFSocket name server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcopyregisteredsocketsignature(_:_:_:_:_:))*