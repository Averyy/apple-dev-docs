# SCNetworkConnectionCallBack

**Framework**: System Configuration  
**Kind**: typealias  
**Role**: Type Alias

The type of callback function used when a status event is delivered.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias SCNetworkConnectionCallBack = (SCNetworkConnection, SCNetworkConnectionStatus, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(const struct __SCNetworkConnection *, enum SCNetworkConnectionStatus, void *) SCNetworkConnectionCallBack;
```

## Parameters

- `connection`: The network connection.
- `status`: The connection status.
- `info`: Application-specific information.

## Topics

### Fields
- [connection](./api-1807883-connection.md)
  The network connection.
- [status](./api-1807884-status.md)
  The connection status.

## See Also

### Data Types
- [class SCNetworkConnection](./scnetworkconnection.md)
  The handle to manage a connection-oriented service.
- [struct SCNetworkConnectionContext](./scnetworkconnectioncontext.md)
  A structure containing user-specified data and callbacks for a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncallback)*