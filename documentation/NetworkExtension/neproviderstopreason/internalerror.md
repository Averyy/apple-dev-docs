# NEProviderStopReason.internalError

**Framework**: Network Extension  
**Kind**: case

The provider encountered an internal error.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- tvOS 18.1+
- visionOS 2.1+

## Declaration

```swift
case internalError
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neproviderstopreason/internalerror)*