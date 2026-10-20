# Socket Name Server Utilities

**Framework**: Core Foundation  
**Role**: API Collection

#### Overview

Name server functionality is currently inoperable in macOS.

## Topics

### Core Foundation Socket Name Server Utilities Miscellaneous Functions
- [func CFSocketCopyRegisteredSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<CFSocketSignature>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](./cfsocketcopyregisteredsocketsignature%28_,_,_,_,_%29.md)
  Returns a socket signature registered with a CFSocket name server.
- [func CFSocketCopyRegisteredValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError](./cfsocketcopyregisteredvalue%28_,_,_,_,_%29.md)
  Returns a value registered with a CFSocket name server.
- [func CFSocketGetDefaultNameRegistryPortNumber() -> UInt16](./cfsocketgetdefaultnameregistryportnumber%28%29.md)
  Returns the default port number with which to connect to a CFSocket name server.
- [func CFSocketRegisterSocketSignature(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, UnsafePointer<CFSocketSignature>!) -> CFSocketError](./cfsocketregistersocketsignature%28_,_,_,_%29.md)
  Registers a socket signature with a CFSocket name server.
- [func CFSocketRegisterValue(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!, CFPropertyList!) -> CFSocketError](./cfsocketregistervalue%28_,_,_,_%29.md)
  Registers a property-list value with a CFSocket name server.
- [func CFSocketSetDefaultNameRegistryPortNumber(UInt16)](./cfsocketsetdefaultnameregistryportnumber%28_%29.md)
  Sets the default port number with which to connect to a CFSocket name server.
- [func CFSocketUnregister(UnsafePointer<CFSocketSignature>!, CFTimeInterval, CFString!) -> CFSocketError](./cfsocketunregister%28_,_,_%29.md)
  Unregisters a value or socket signature with a CFSocket name server.
### Constants
- [CFSocket Name Server Keys](./cfsocket-name-server-keys.md)
  Not used.

## See Also

### Utilities
- [Base Utilities](./base-utilities.md)
- [Byte-Order Utilities](./byte-order-utilities.md)
- [Core Foundation URL Access Utilities](./core-foundation-url-access-utilities.md)
- [Preferences Utilities](./preferences-utilities.md)
- [Time Utilities](./time-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/socket-name-server-utilities)*