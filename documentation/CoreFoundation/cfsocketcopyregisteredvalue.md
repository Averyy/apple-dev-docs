# CFSocketCopyRegisteredValue(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a value registered with a CFSocket name server.

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
func CFSocketCopyRegisteredValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ value: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError
```

#### Return Value

An error code indicating success or failure.

## Parameters

- `nameServerSignature`: The socket signature for the name server. If  , this function contacts the default server, which is assumed to be a local process using TCP/IP to listen on the port number returned from  . If   is incomplete, the missing values are replaced with the default server’s values, if appropriate.
- `timeout`: The time to wait for the server to accept a connection and to reply to the registration request.
- `name`: The name of the registered value to return.
- `value`: A pointer to the property list object into which the retrieved value should be copied.
- `nameServerAddress`: A pointer to a CFData object into which the name server’s address is copied. Pass   if you do not want the server’s address.

## See Also

- [func CFSocketCopyRegisteredSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](cfsocketcopyregisteredsocketsignature(_:_:_:_:_:).md)
  Returns a socket signature registered with a CFSocket name server.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcopyregisteredvalue(_:_:_:_:_:))*