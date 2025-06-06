# SCNetworkConnectionCallBack

**Framework**: System Configuration  
**Kind**: typealias

The type of callback function used when a status event is delivered.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias SCNetworkConnectionCallBack = (SCNetworkConnection, SCNetworkConnectionStatus, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `connection`: The network connection.
- `status`: The connection status.
- `info`: Application-specific information.

## Topics

### Fields
- [connection](1807883-connection.md)
  The network connection.
- [status](1807884-status.md)
  The connection status.

## See Also

- [class SCNetworkConnection](scnetworkconnection.md)
  The handle to manage a connection-oriented service.
- [struct SCNetworkConnectionContext](scnetworkconnectioncontext.md)
  A structure containing user-specified data and callbacks for a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectioncallback)*