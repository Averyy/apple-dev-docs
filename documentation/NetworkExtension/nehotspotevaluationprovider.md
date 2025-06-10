# NEHotspotEvaluationProvider

**Framework**: Network Extension  
**Kind**: protocol

A protocol that defines methods and properties your extension implements to handle evaluate and filter scan list commands.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol NEHotspotEvaluationProvider : NEAppExtension
```

#### Overview

Conform to this protocol in your hotspot helper app extension.

## Topics

### Managing provider life cycle
- [func start() async -> Bool](nehotspotevaluationprovider/start.md)
  Tells the extension to start the evaluation provider, in response to a request from the framework.
- [func stop(reason: NEProviderStopReason) async](nehotspotevaluationprovider/stop(reason:).md)
  Tells the exension to stop the evaluation provider, in response to a request from the framework.
- [enum NEProviderStopReason](neproviderstopreason.md)
  Reasons why the provider extension was stopped.
### Sending commands to the provider
- [func handleCommand(NEHotspotHelperCommand) async -> NEHotspotHelperResponse](nehotspotevaluationprovider/handlecommand(_:).md)
  Handles a given hotspot command, in response to a request from the framework.
- [class NEHotspotHelperCommand](nehotspothelpercommand.md)
  A command for the hotspot helper to handle.
### Providing a network name
- [var localizedDisplayName: String](nehotspotevaluationprovider/localizeddisplayname.md)
  A localized string that the system UI uses for annotation of the Wi-Fi network.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [NEAppExtension](neappextension.md)

## See Also

- [class NEHotspotManager](nehotspotmanager.md)
  A class that you use to enable or disable the hotspot evaluation and authentication provider extensions.
- [protocol NEHotspotAuthenticationProvider](nehotspotauthenticationprovider.md)
  A protocol that defines methods that your extension adopts to start and stop the extension, and to handle commands to authenticate with the hotspot network.
- [class NEHotspotEvaluationProviderConfiguration](nehotspotevaluationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension evaluation providers.
- [class NEHotspotAuthenticationProviderConfiguration](nehotspotauthenticationproviderconfiguration.md)
  A class that defines configuration options for use in NetworkExtension authentication providers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotevaluationprovider)*