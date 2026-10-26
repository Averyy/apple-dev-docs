# CNCopyCurrentNetworkInfo

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the current network information for a given network interface.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0

> **Deprecated**: Use [`fetchCurrent(completionHandler:)`](../NetworkExtension/nehotspotnetwork/fetchcurrent%28completionhandler%29.md) instead.

## Declaration

```c
CFDictionaryRefCNCopyCurrentNetworkInfo(CFStringRef interfaceName);
```

#### Return Value

A dictionary containing the interface’s current network information, provided certain requirements are met (see Discussion section). If the requirements are not met, the return value is either a dictionary with pseudo-values or `NULL`. If an error occurs, the return value is `NULL`.

#### Discussion

The returned dictionary contains the following keys and values:

| Key | Value type |
| --- | --- |
| [`kCNNetworkInfoKeySSIDData`](./kcnnetworkinfokeyssiddata.md) | [`CFData`](../CoreFoundation/cfdata.md) |
| [`kCNNetworkInfoKeySSID`](./kcnnetworkinfokeyssid.md) | [`CFString`](../CoreFoundation/cfstring.md) |
| [`kCNNetworkInfoKeyBSSID`](./kcnnetworkinfokeybssid.md) | [`CFString`](../CoreFoundation/cfstring.md) |

Ownership of the returned dictionary follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029). You are responsible for releasing the returned value.

#### Discussion

The requesting app must meet one of the following requirements:

- The app uses [Core Location](../CoreLocation/CoreLocation.md), and has the user’s authorization to use location information.
- The app uses the [`NEHotspotConfiguration`](../NetworkExtension/nehotspotconfiguration.md) API to configure the current Wi-Fi network.
- The app has an active VPN configuration installed.
- The app has an active [`NEDNSSettingsManager`](../NetworkExtension/nednssettingsmanager.md) configuration installed.

If the requesting app is a Mac app built with Mac Catalyst, it must meet the following requirements:

- The app uses [Core Location](../CoreLocation/CoreLocation.md), and has the user’s authorization to use location information.
- The app includes the [`Access Wi-Fi Information Entitlement`](../BundleResources/entitlements/com.apple.developer.networking.wifi-info.md).
- The app runs in macOS 11 or later.

An app that fails to meet the above requirements receives the following return value:

- An app linked against iOS 12 or earlier receives a dictionary with pseudo-values. In this case, the SSID is `Wi-Fi` (or `WLAN` in China mainland), and the BSSID is `00:00:00:00:00:00`.
- An app linked against iOS 13 or later receives `NULL`.

> ❗ **Important**:  To use this function, an app linked against iOS 12 or later must enable the Access WiFi Information capability in Xcode. For more information, see [`Access Wi-Fi Information Entitlement`](../BundleResources/entitlements/com.apple.developer.networking.wifi-info.md). Calling this function without the entitlement always returns `NULL` when linked against iOS 12 or later.

## Parameters

- `interfaceName`: The network interface name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/cncopycurrentnetworkinfo)*