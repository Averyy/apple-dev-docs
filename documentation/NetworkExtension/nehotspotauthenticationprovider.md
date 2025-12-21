# NEHotspotAuthenticationProvider

**Framework**: Network Extension  
**Kind**: protocol

A protocol that defines methods that your extension adopts to start and stop the extension, and to handle commands to authenticate with the hotspot network.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol NEHotspotAuthenticationProvider : AppExtension
```

#### Overview

Conform to this protocol in your hotspot helper app extension to handle the hotspot commands [`NEHotspotHelperCommandType.authenticate`](nehotspothelpercommandtype/authenticate.md), [`NEHotspotHelperCommandType.maintain`](nehotspothelpercommandtype/maintain.md), [`NEHotspotHelperCommandType.presentUI`](nehotspothelpercommandtype/presentui.md), and [`NEHotspotHelperCommandType.logoff`](nehotspothelpercommandtype/logoff.md).

## Topics

### Managing provider life cycle
- [func start() async -> Bool](nehotspotauthenticationprovider/start.md)
  Tells the extension to start the authentication provider, in response to a request from the framework.
- [func stop(reason: NEProviderStopReason) async](nehotspotauthenticationprovider/stop(reason:).md)
  Tells the exension to stop the authentication provider, in response to a request from the framework.
- [enum NEProviderStopReason](neproviderstopreason.md)
  Reasons why the provider extension was stopped.
### Sending commands to the provider
- [func handleCommand(NEHotspotHelperCommand) async -> NEHotspotHelperResponse](nehotspotauthenticationprovider/handlecommand(_:).md)
  Handles a given hotspot command, in response to a request from the framework.
- [class NEHotspotHelperCommand](nehotspothelpercommand.md)
  A command for the hotspot helper to handle.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [class NEHotspotManager](nehotspotmanager.md)
  A class that you use to enable or disable the hotspot evaluation and authentication provider extensions.
- [protocol NEHotspotEvaluationProvider](nehotspotevaluationprovider.md)
  A protocol that defines methods and properties your extension implements to handle evaluate and filter scan list commands.
- [class NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension evaluation providers.
- [class NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension authentication providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotauthenticationprovider)*