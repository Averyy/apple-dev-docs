# SCNetworkConnectionContext

**Framework**: System Configuration  
**Kind**: struct

A structure containing user-specified data and callbacks for a network connection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct SCNetworkConnectionContext
```

## Topics

### Initializers
- [init()](scnetworkconnectioncontext/init.md)
  Creates a network connection context.
- [init(version: CFIndex, info: UnsafeMutableRawPointer?, retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?, release: ((UnsafeRawPointer) -> Void)?, copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?)](scnetworkconnectioncontext/init(version:info:retain:release:copydescription:).md)
  Creates a network connection context with the specified values.
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer) -> Unmanaged<CFString>)?](scnetworkconnectioncontext/copydescription.md)
  The callback used to provide a description of the `info` field.
- [var info: UnsafeMutableRawPointer?](scnetworkconnectioncontext/info.md)
  A C pointer to a user-specified block of data.
- [var release: ((UnsafeRawPointer) -> Void)?](scnetworkconnectioncontext/release.md)
  The calllback used to remove a retain previously added for the info field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value may be `NULL`.
- [var retain: ((UnsafeRawPointer) -> UnsafeRawPointer)?](scnetworkconnectioncontext/retain.md)
  The callback used to add a retain for the info field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The value may be `NULL`.
- [var version: CFIndex](scnetworkconnectioncontext/version.md)
  The version number of the structure type being passed in as a parameter to the [`SCNetworkConnectionCreateWithServiceID(_:_:_:_:)`](scnetworkconnectioncreatewithserviceid(_:_:_:_:).md) function. This structure is version `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class SCNetworkConnection](scnetworkconnection.md)
  The handle to manage a connection-oriented service.
- [typealias SCNetworkConnectionCallBack](scnetworkconnectioncallback.md)
  The type of callback function used when a status event is delivered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncontext)*