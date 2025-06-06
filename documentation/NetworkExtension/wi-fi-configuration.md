# Wi-Fi configuration

**Framework**: Network Extension

Add persistent Wi-Fi configurations, or temporarily move the device to a specific Wi-Fi network.

#### Overview

Using [`NEHotspotConfigurationManager`](nehotspotconfigurationmanager.md), you can programmatically create two different types of Wi-Fi configurations:

- Persistent configurations, which are equivalent to the user joining a Wi-Fi network using the Settings app
- Join-once configurations, which temporarily move the device to a specific Wi-Fi network

The user must explicitly authorize both of these operations.

This API can help with a wide variety of tasks. For example, you can use it to help a user join a specific Wi-Fi network, like the hotspot at a local coffee shop, or to set up an accessory that uses Wi-Fi.

[`NEHotspotConfigurationManager`](nehotspotconfigurationmanager.md) supports a variety of authentication models:

- SSID with no authentication
- SSID with password-based authentication (WEP, WPA, and WPA2)
- SSID with EAP authentication
- Hotspot 2.0 with EAP authentication

[`NEHotspotConfigurationManager`](nehotspotconfigurationmanager.md) is only supported on iOS. For macOS, use the [`Core WLAN`](https://developer.apple.com/documentation/CoreWLAN) framework, which provides a full-featured Wi-Fi configuration and management API.

## Topics

### Essentials
- [Hotspot Configuration Entitlement](../BundleResources/Entitlements/com.apple.developer.networking.HotspotConfiguration.md)
  A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.
### Wi-Fi network configuration
- [class NEHotspotConfigurationManager](nehotspotconfigurationmanager.md)
  A manager that applies and removes hotspot configurations of Wi-Fi networks.
- [class NEHotspotConfiguration](nehotspotconfiguration.md)
  Configuration settings for a Wi-Fi network.
- [class NEHotspotEAPSettings](nehotspoteapsettings.md)
  Extensible Authentication Protocol settings for configuring WPA and WPA2 enterprise Wi-Fi networks.
- [class NEHotspotHS20Settings](nehotspoths20settings.md)
  Settings for configuring Hotspot 2.0 Wi-Fi networks.

## See Also

- [Configuring a Wi-Fi accessory to join a network](configuring-a-wi-fi-accessory-to-join-a-network.md)
  Associate an iOS device with an accessory’s network to deliver network configuration information.
- [Hotspot helper](hotspot-helper.md)
  Integrate your app with the iOS hotspot network subsystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/wi-fi-configuration)*