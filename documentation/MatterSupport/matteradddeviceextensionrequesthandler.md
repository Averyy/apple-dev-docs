# MatterAddDeviceExtensionRequestHandler

**Framework**: MatterSupport  
**Kind**: class

The object that handles configuration and commissioning of a device into an ecosystem.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
@objc
class MatterAddDeviceExtensionRequestHandler
```

## Mentions

- [Adding Matter support to your ecosystem](adding-matter-support-to-your-ecosystem.md)

#### Overview

This class facilitates the user interface flow during the setup of a new Matter device. Subclass this class and override its methods, except for `beginRequest(with:)`. The principal class for the app’s extension declared by the [`NSPrincipalClass`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPrincipalClass) in the extension plist must inherit from this base class.

If the [`MatterAddDeviceRequest.Topology`](matteradddevicerequest/topology-swift.struct.md) object in the request has two or more homes, the user interface flow displays a picker to allow selection of a home. If the object contains one home, that home is the selected home and the user interface flow doesn’t display a picker. If the object contains no home, then the user interface flow doesn’t display a picker, and any methods take a home parameter receive `nil`.

> **Note**: Don’t call `super` within the overridden method.

Don’t call `super` within the overridden method.

## Topics

### Creating the request handler
- [init()](matteradddeviceextensionrequesthandler/init.md)
### Configuring and validating the device
- [func configureDevice(named: String, in: MatterAddDeviceRequest.Room?) async](matteradddeviceextensionrequesthandler/configuredevice(named:in:).md)
  Configures the device with selected attributes.
- [func validateDeviceCredential(MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws](matteradddeviceextensionrequesthandler/validatedevicecredential(_:).md)
  Performs verification and attestation checks.
- [MatterAddDeviceExtensionRequestHandler.DeviceCredential](matteradddeviceextensionrequesthandler/devicecredential.md)
  A collection of device credentials the device presents during commissioning.
- [func rooms(in: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room]](matteradddeviceextensionrequesthandler/rooms(in:).md)
  Provides rooms that correspond to a home in the device setup.
### Commissioning the device
- [func commissionDevice(in: MatterAddDeviceRequest.Home?, onboardingPayload: String, commissioningID: UUID) async throws](matteradddeviceextensionrequesthandler/commissiondevice(in:onboardingpayload:commissioningid:).md)
  Commissions the device with the onboarding payload.
### Selecting the Thread network
- [func selectThreadNetwork(from: [MatterAddDeviceExtensionRequestHandler.ThreadScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/selectthreadnetwork(from:).md)
  Provides the visible Thread networks to the device.
- [MatterAddDeviceExtensionRequestHandler.ThreadScanResult](matteradddeviceextensionrequesthandler/threadscanresult.md)
  A result of a Thread-scan operation performed on the device
- [MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/threadnetworkassociation.md)
  The description of an association to a Thread network.
### Selecting the Wi-Fi network
- [func selectWiFiNetwork(from: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/selectwifinetwork(from:).md)
  Provides the visible Wi-Fi networks to the Matter device.
- [MatterAddDeviceExtensionRequestHandler.WiFiScanResult](matteradddeviceextensionrequesthandler/wifiscanresult.md)
  A result of a Wi-Fi-scan operation performed on the device
- [MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation](matteradddeviceextensionrequesthandler/wifinetworkassociation.md)
  The description of an association to a Wi-Fi network.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Adding Matter support to your ecosystem](adding-matter-support-to-your-ecosystem.md)
  Allow people to add Matter accessories to your platform.
- [struct MatterAddDeviceRequest](matteradddevicerequest.md)
  A request that adds and sets up a device into an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler)*