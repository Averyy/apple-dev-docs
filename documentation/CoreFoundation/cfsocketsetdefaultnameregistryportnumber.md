# CFSocketSetDefaultNameRegistryPortNumber(_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the default port number with which to connect to a CFSocket name server.

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
func CFSocketSetDefaultNameRegistryPortNumber(_ port: UInt16)
```

#### Discussion

If you do not provide a name server signature or leave out the socket address in the signature when calling one of the name registry functions, such as [`CFSocketRegisterSocketSignature(_:_:_:_:)`](cfsocketregistersocketsignature(_:_:_:_:).md), `port` will be used for the connection.

## Parameters

- `port`: The port number to use to connect to the CFSocket name server.

## See Also

- [func CFSocketCopyRegisteredSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](cfsocketcopyregisteredsocketsignature(_:_:_:_:_:).md)
  Returns a socket signature registered with a CFSocket name server.
- [func CFSocketCopyRegisteredValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](cfsocketcopyregisteredvalue(_:_:_:_:_:).md)
  Returns a value registered with a CFSocket name server.
- [func CFSocketGetDefaultNameRegistryPortNumber() -> UInt16](cfsocketgetdefaultnameregistryportnumber().md)
  Returns the default port number with which to connect to a CFSocket name server.
- [func CFSocketRegisterSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafePointer<CFSocketSignature>!) -> CFSocketError](cfsocketregistersocketsignature(_:_:_:_:).md)
  Registers a socket signature with a CFSocket name server.
- [func CFSocketRegisterValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, CFPropertyList!) -> CFSocketError](cfsocketregistervalue(_:_:_:_:).md)
  Registers a property-list value with a CFSocket name server.
- [func CFSocketUnregister(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!) -> CFSocketError](cfsocketunregister(_:_:_:).md)
  Unregisters a value or socket signature with a CFSocket name server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketsetdefaultnameregistryportnumber(_:))*