# NEHotspotConfigurationManager

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A manager that applies and removes hotspot configurations of Wi-Fi networks.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class NEHotspotConfigurationManager
```

```objc
@interface NEHotspotConfigurationManager : NSObject
```

## Overview

When your app creates a new hotspot configuration using [`NEHotspotConfiguration`](./nehotspotconfiguration.md) and applies it to a Wi-Fi network or attempts to update a previously configured network, the device prompts the user for approval. Without explicit user consent, your app can’t make configuration changes.

Your app can use [`removeConfiguration(forHS20DomainName:)`](./nehotspotconfigurationmanager/removeconfiguration%28forhs20domainname%29.md) or [`removeConfiguration(forSSID:)`](./nehotspotconfigurationmanager/removeconfiguration%28forssid%29.md) to delete a configuration that it has added, but not a configuration added by another app or user. The user can also delete configured networks using Settings > Wi-Fi.

When your app is uninstalled, iOS removes the configurations of all networks your app has configured, including their keychain entries.

Hotspot Configuration Manager errors are listed in [`NEHotspotConfigurationError`](./nehotspotconfigurationerror.md).

> ❗ **Important**:  To use the [`NEHotspotConfigurationManager`](./nehotspotconfigurationmanager.md) class, you must enable the Hotspot Configuration capability in Xcode. For more information, see [`Hotspot Configuration Entitlement`](../BundleResources/entitlements/com.apple.developer.networking.hotspotconfiguration.md).

## Topics

### Creating configurations
- [class var shared: NEHotspotConfigurationManager](./nehotspotconfigurationmanager/shared.md)
  Instantiates [`NEHotspotConfigurationManager`](./nehotspotconfigurationmanager.md) as a singleton, so it can be shared.
- [func apply(NEHotspotConfiguration, completionHandler: (((any Error)?) -> Void)?)](./nehotspotconfigurationmanager/apply%28_,completionhandler%29.md)
  Adds or updates a Wi-Fi network configuration after prompting the user for permission, and then attempts to join the network under certain conditions.
### Getting a list of configurations
- [func getConfiguredSSIDs(completionHandler: ([String]) -> Void)](./nehotspotconfigurationmanager/getconfiguredssids%28completionhandler%29.md)
  Submits a completion handler the configuration manager calls to send your app the names of the SSIDs or Wi-Fi hotspot domains in the configuration.
### Removing configuration
- [func removeConfiguration(forHS20DomainName: String)](./nehotspotconfigurationmanager/removeconfiguration%28forhs20domainname%29.md)
  Removes a Wi-Fi hotspot configuration, identified by a Hotspot 2.0 domain name, that your app previously added.
- [func removeConfiguration(forSSID: String)](./nehotspotconfigurationmanager/removeconfiguration%28forssid%29.md)
  Removes a Wi-Fi configuration, identified by an SSID, that your app previously added.
### Errors
- [let NEHotspotConfigurationErrorDomain: String](./nehotspotconfigurationerrordomain.md)
  The domain string for errors involving hotspot configuration.
- [enum NEHotspotConfigurationError](./nehotspotconfigurationerror.md)
  Error values returned by hotspot configuration manager methods.
### Entitlements
- [Hotspot Configuration Entitlement](../BundleResources/entitlements/com.apple.developer.networking.hotspotconfiguration.md)
  A Boolean value indicating whether your app can use the hotspot manager to configure Wi-Fi networks.
### Instance Methods
- [func joinAccessoryHotspot(ASAccessory, passphrase: String, completionHandler: (((any Error)?) -> Void)?)](./nehotspotconfigurationmanager/joinaccessoryhotspot%28_,passphrase,completionhandler%29.md)
- [func joinAccessoryHotspotWithoutSecurity(ASAccessory, completionHandler: (((any Error)?) -> Void)?)](./nehotspotconfigurationmanager/joinaccessoryhotspotwithoutsecurity%28_,completionhandler%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Wi-Fi network configuration
- [class NEHotspotConfiguration](./nehotspotconfiguration.md)
  Configuration settings for a Wi-Fi network.
- [class NEHotspotEAPSettings](./nehotspoteapsettings.md)
  Extensible Authentication Protocol settings for configuring WPA and WPA2 enterprise Wi-Fi networks.
- [class NEHotspotHS20Settings](./nehotspoths20settings.md)
  Settings for configuring Hotspot 2.0 Wi-Fi networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotconfigurationmanager)*