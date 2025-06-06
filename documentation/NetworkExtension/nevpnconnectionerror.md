# NEVPNConnectionError

**Framework**: Network Extension  
**Kind**: enum

Error codes specific to VPN connections.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEVPNConnectionError
```

## Topics

### General error codes
- [NEVPNConnectionError.overslept](nevpnconnectionerror/overslept.md)
  An error code that indicates the system slept for an extended period of time, causing the VPN connection to terminate.
- [NEVPNConnectionError.noNetworkAvailable](nevpnconnectionerror/nonetworkavailable.md)
  An error code that indicates the VPN connection failed because the system isn’t connected to a network.
- [NEVPNConnectionError.unrecoverableNetworkChange](nevpnconnectionerror/unrecoverablenetworkchange.md)
  An error code that indicates network conditions changed such that the VPN connection needed to terminate.
- [NEVPNConnectionError.configurationFailed](nevpnconnectionerror/configurationfailed.md)
  An error code that indicates the VPN connection failed because the configuration is invalid.
- [NEVPNConnectionError.authenticationFailed](nevpnconnectionerror/authenticationfailed.md)
  An error code that indicates the VPN connection failed because the VPN server rejected the user credentials.
- [NEVPNConnectionError.configurationNotFound](nevpnconnectionerror/configurationnotfound.md)
  An error code that indicates the VPN connection failed because the system couldn’t find a configuration.
- [NEVPNConnectionError.negotiationFailed](nevpnconnectionerror/negotiationfailed.md)
  An error code that indicates the VPN connection failed because the negotiation failed.
### VPN server error codes
- [NEVPNConnectionError.serverAddressResolutionFailed](nevpnconnectionerror/serveraddressresolutionfailed.md)
  An error code that indicates the VPN connection failed because the system couldn’t determine the VPN server address.
- [NEVPNConnectionError.serverNotResponding](nevpnconnectionerror/servernotresponding.md)
  An error code that indicates the VPN connection failed because the VPN server isn’t responding.
- [NEVPNConnectionError.serverDead](nevpnconnectionerror/serverdead.md)
  An error code that indicates the VPN connection failed because the VPN server has stopped responding.
- [NEVPNConnectionError.serverDisconnected](nevpnconnectionerror/serverdisconnected.md)
  An error code that indicates the VPN connection failed because the VPN server terminated the connection.
### Plugin error codes
- [NEVPNConnectionError.pluginFailed](nevpnconnectionerror/pluginfailed.md)
  An error code that indicates the VPN plugin failed unexpectedly.
- [NEVPNConnectionError.pluginDisabled](nevpnconnectionerror/plugindisabled.md)
  An error code that indicates the VPN plugin isn’t available or needs an update.
### Client certificate error codes
- [NEVPNConnectionError.clientCertificateInvalid](nevpnconnectionerror/clientcertificateinvalid.md)
  An error code that indicates the client certfiicate is invalid.
- [NEVPNConnectionError.clientCertificateNotYetValid](nevpnconnectionerror/clientcertificatenotyetvalid.md)
  An error code that indicates the client certfiicate won’t be valid until some time in the future.
- [NEVPNConnectionError.clientCertificateExpired](nevpnconnectionerror/clientcertificateexpired.md)
  An error code that indicates the client certfiicate’s validity period has passed.
### Server certificate error codes
- [NEVPNConnectionError.serverCertificateInvalid](nevpnconnectionerror/servercertificateinvalid.md)
  An error code that indicates the server certfiicate is invalid.
- [NEVPNConnectionError.serverCertificateNotYetValid](nevpnconnectionerror/servercertificatenotyetvalid.md)
  An error code that indicates the server certfiicate won’t be valid until some time in the future.
- [NEVPNConnectionError.serverCertificateExpired](nevpnconnectionerror/servercertificateexpired.md)
  An error code that indicates the server certfiicate’s validity period has passed.
### Initializers
- [init?(rawValue: Int)](nevpnconnectionerror/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func fetchLastDisconnectError(completionHandler: ((any Error)?) -> Void)](nevpnconnection/fetchlastdisconnecterror(completionhandler:).md)
  Retrives the most recent error that caused the VPN to disconnect.
- [let NEVPNConnectionErrorDomain: String](nevpnconnectionerrordomain.md)
  The domain for errors resulting from VPN connection calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnectionerror)*