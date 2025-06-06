# MatterSupport

**Framework**: MatterSupport  
**Kind**: module

Coordinate and control compatible smart home accessories.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 14.0+
- macOS 14.0+
- visionOS 1.0+

#### Overview

Matter is a smart home connectivity standard that gives your app the ability to control devices from a wide variety of manufacturers and across platforms. Adopt this framework in your app to add compatible devices to your ecosystem, then use [`Matter`](https://developer.apple.com/documentation/Matter) to commission and control them.

> ❗ **Important**: Calls to this framework return errors to Mac apps built with Mac Catalyst.

Calls to this framework return errors to Mac apps built with Mac Catalyst.

## Topics

### Adding a device
- [Adding Matter support to your ecosystem](adding-matter-support-to-your-ecosystem.md)
  Allow people to add Matter accessories to your platform.
- [struct MatterAddDeviceRequest](matteradddevicerequest.md)
  A request that adds and sets up a device into an ecosystem.
- [class MatterAddDeviceExtensionRequestHandler](matteradddeviceextensionrequesthandler.md)
  The object that handles configuration and commissioning of a device into an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MatterSupport)*