# NEVPNConnection

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object to start and stop a Personal VPN connection and get its status.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NEVPNConnection
```

```objc
@interface NEVPNConnection : NSObject
```

## Overview

[`NEVPNConnection`](./nevpnconnection.md) objects are not instantiated directly. Instead, each `NEVPNManager` object has an associated [`NEVPNConnection`](./nevpnconnection.md) object as a read-only property.

The [`NEVPNConnection`](./nevpnconnection.md) class provides methods for starting and stopping the VPN programmatically. The other way that the VPN can be started and stopped is through VPN On Demand. See the `onDemandRules` property in [`NEVPNManager`](./nevpnmanager.md) and [`NEOnDemandRule`](./neondemandrule.md).

Instances of this class are thread safe.

## Topics

### Controlling the VPN connection
- [func startVPNTunnel() throws](./nevpnconnection/startvpntunnel%28%29.md)
  Start the process of connecting the VPN.
- [func startVPNTunnel(options: [String : NSObject]?) throws](./nevpnconnection/startvpntunnel%28options%29.md)
  Start the process of connecting the VPN.
- [let NEVPNConnectionStartOptionUsername: String](./nevpnconnectionstartoptionusername.md)
- [let NEVPNConnectionStartOptionPassword: String](./nevpnconnectionstartoptionpassword.md)
- [func stopVPNTunnel()](./nevpnconnection/stopvpntunnel%28%29.md)
  Start the process of disconnecting the VPN.
### Getting VPN connection status
- [var manager: NEVPNManager](./nevpnconnection/manager.md)
- [var status: NEVPNStatus](./nevpnconnection/status.md)
  The current status of the VPN connection.
- [enum NEVPNStatus](./nevpnstatus.md)
  The possible states of a VPN connection.
- [var connectedDate: Date?](./nevpnconnection/connecteddate.md)
  The date and time when the connection status changed to `NEVPNStatusConnected`.
### Notifications
- [static let NEVPNStatusDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/nevpnstatusdidchange.md)
  Posted when the status of the VPN connection changes.
- [NEVPNStatusDidChangeNotification](./nevpnstatusdidchangenotification.md)
  Posted when the status of the VPN connection changes.
### Handling errors
- [func fetchLastDisconnectError(completionHandler: ((any Error)?) -> Void)](./nevpnconnection/fetchlastdisconnecterror%28completionhandler%29.md)
  Retrives the most recent error that caused the VPN to disconnect.
- [let NEVPNConnectionErrorDomain: String](./nevpnconnectionerrordomain.md)
  The domain for errors resulting from VPN connection calls.
- [enum NEVPNConnectionError](./nevpnconnectionerror.md)
  Error codes specific to VPN connections.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NETunnelProviderSession](./netunnelprovidersession.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### VPN control
- [class NETunnelProviderSession](./netunnelprovidersession.md)
  An object to start and stop a tunnel connection and get its status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection)*