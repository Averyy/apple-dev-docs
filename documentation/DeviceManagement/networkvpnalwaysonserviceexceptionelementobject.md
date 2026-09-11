# NetworkVPNAlwaysOnServiceExceptionElementObject

**Framework**: Device Management  
**Kind**: dictionary

An array that contains an arbitrary number of service exceptions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
object NetworkVPNAlwaysOnServiceExceptionElementObject
```

## Properties

- `Action` (string) *(required)*: The action to take with network connections from the named service.
- `ServiceName` (string) *(required)*: The name of a service that’s exempt from Always On VPN. `CellularServices` exempts `VoLTE`, `IMS`, `MMS`, and Wi-Fi calling. `DeviceCommunication` exempts network traffic used for communicating with devices connected via USB or Wi-Fi.

## See Also

- [object NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject](networkvpnalwaysonallowedcaptivenetworkpluginelementobject.md)
  The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- [object NetworkVPNAlwaysOnApplicationExceptionElementObject](networkvpnalwaysonapplicationexceptionelementobject.md)
  An array that contains an arbitrary number of apps whose connections occur outside the VPN.
- [object NetworkVPNAlwaysOnTunnelConfigurationElementObject](networkvpnalwaysontunnelconfigurationelementobject.md)
  An array that contains an arbitrary number of tunnel configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonserviceexceptionelementobject)*