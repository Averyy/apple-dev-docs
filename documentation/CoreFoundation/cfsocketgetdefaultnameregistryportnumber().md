# CFSocketGetDefaultNameRegistryPortNumber()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the default port number with which to connect to a CFSocket name server.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFSocketGetDefaultNameRegistryPortNumber() -> UInt16
```

```c
extern UInt16 CFSocketGetDefaultNameRegistryPortNumber();
```

#### Return Value

The default port number with which to connect to a CFSocket name server.

#### Discussion

If you do not provide a name server signature or leave out the socket address in the signature when calling one of the name registry functions, such as [`CFSocketRegisterSocketSignature(_:_:_:_:)`](./cfsocketregistersocketsignature%28_,_,_,_%29.md), the returned port number is used for the connection.

## See Also

### Core Foundation Socket Name Server Utilities Miscellaneous Functions
- [func CFSocketCopyRegisteredSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](./cfsocketcopyregisteredsocketsignature%28_,_,_,_,_%29.md)
  Returns a socket signature registered with a CFSocket name server.
- [func CFSocketCopyRegisteredValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](./cfsocketcopyregisteredvalue%28_,_,_,_,_%29.md)
  Returns a value registered with a CFSocket name server.
- [func CFSocketRegisterSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafePointer<CFSocketSignature>!) -> CFSocketError](./cfsocketregistersocketsignature%28_,_,_,_%29.md)
  Registers a socket signature with a CFSocket name server.
- [func CFSocketRegisterValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, CFPropertyList!) -> CFSocketError](./cfsocketregistervalue%28_,_,_,_%29.md)
  Registers a property-list value with a CFSocket name server.
- [func CFSocketSetDefaultNameRegistryPortNumber(UInt16)](./cfsocketsetdefaultnameregistryportnumber%28_%29.md)
  Sets the default port number with which to connect to a CFSocket name server.
- [func CFSocketUnregister(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!) -> CFSocketError](./cfsocketunregister%28_,_,_%29.md)
  Unregisters a value or socket signature with a CFSocket name server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketgetdefaultnameregistryportnumber())*