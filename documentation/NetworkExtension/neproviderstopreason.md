# NEProviderStopReason

**Framework**: Network Extension  
**Kind**: enum

Reasons why the provider extension was stopped.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum NEProviderStopReason
```

#### Overview

`NEProviderStopReasonUserLogout` and `NEProviderStopReasonUserSwitch` are available only in macOS.

## Topics

### Stop Reasons
- [NEProviderStopReason.none](neproviderstopreason/none.md)
  No specific reason.
- [NEProviderStopReason.userInitiated](neproviderstopreason/userinitiated.md)
  The user stopped the provider extension.
- [NEProviderStopReason.providerFailed](neproviderstopreason/providerfailed.md)
  The provider failed to function correctly.
- [NEProviderStopReason.noNetworkAvailable](neproviderstopreason/nonetworkavailable.md)
  No network connectivity is currently available.
- [NEProviderStopReason.unrecoverableNetworkChange](neproviderstopreason/unrecoverablenetworkchange.md)
  The device’s network connectivity changed.
- [NEProviderStopReason.providerDisabled](neproviderstopreason/providerdisabled.md)
  The provider was disabled.
- [NEProviderStopReason.authenticationCanceled](neproviderstopreason/authenticationcanceled.md)
  The authentication process was canceled.
- [NEProviderStopReason.configurationFailed](neproviderstopreason/configurationfailed.md)
  The configuration is invalid.
- [NEProviderStopReason.idleTimeout](neproviderstopreason/idletimeout.md)
  The session timed out.
- [NEProviderStopReason.configurationDisabled](neproviderstopreason/configurationdisabled.md)
  The configuration was disabled.
- [NEProviderStopReason.configurationRemoved](neproviderstopreason/configurationremoved.md)
  The configuration was removed.
- [NEProviderStopReason.superceded](neproviderstopreason/superceded.md)
  The configuration was superceded by a higher-priority configuration.
- [NEProviderStopReason.userLogout](neproviderstopreason/userlogout.md)
  The user logged out.
- [NEProviderStopReason.userSwitch](neproviderstopreason/userswitch.md)
  The current console user changed.
- [NEProviderStopReason.appUpdate](neproviderstopreason/appupdate.md)
- [NEProviderStopReason.connectionFailed](neproviderstopreason/connectionfailed.md)
  The connection failed.
- [NEProviderStopReason.sleep](neproviderstopreason/sleep.md)
  A stop reason indicating the configuration enabled disconnect on sleep and the device went to sleep.
- [NEProviderStopReason.internalError](neproviderstopreason/internalerror.md)
  The provider encountered an internal error.
### Initializers
- [init?(rawValue: Int)](neproviderstopreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproviderstopreason)*