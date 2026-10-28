# Discovering a third-party media-streaming device

**Framework**: DeviceDiscoveryExtension  
**Role**: Sample Code  
**Download**: [DiscoveringAThirdPartyMediaStreamingDevice.zip](https://docs-assets.developer.apple.com/published/9dd81d7fe75e/DiscoveringAThirdPartyMediaStreamingDevice.zip)

Build an extension that streams media to a server app in iOS or macOS.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- Xcode 16.0+

## Overview

> **Note**: This sample code project is associated with WWDC22 session [10096: What’s new in privacy](https://developer.apple.com/wwdc22/10096).

### Configure the sample code project

Run either the macOS or iOS server target to emulate a third-party media-streaming receiver. Set the client scheme’s run destination to an iOS 16 device. Run the client and select the emulated device from the system device-picker UI.

## See Also

### Essentials
- [Media Device Discovery Extension](../BundleResources/entitlements/com.apple.developer.media-device-discovery-extension.md)
  An entitlement for an app extension that adds a specific third-party media receiver to a system device-picker UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/discovering-a-third-party-media-streaming-device)*