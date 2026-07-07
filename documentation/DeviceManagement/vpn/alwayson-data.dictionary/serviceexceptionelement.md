# VPN.AlwaysOn.ServiceExceptionElement

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that defines service exceptions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
object VPN.AlwaysOn.ServiceExceptionElement
```

## Properties

- `Action` (string) *(required)*: The action to take with network connections from the named service.
- `ServiceName` (string) *(required)*: The name of a service that’s exempt from Always On VPN. `CellularServices` is available in iOS 11.3 and later; it exempts `VoLTE`, `IMS` and `MMS`. Always On VPN exempts WiFiCalling in iOS 13.4 and later. `DeviceCommunication` is available in iOS 17.4 and later; it exempts network traffic used for communicating with devices connected via USB or Wi-Fi.

## See Also

- [object VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement](vpn/alwayson-data.dictionary/allowedcaptivenetworkpluginelement.md)
  The dictionary for captive network configurations.
- [object VPN.AlwaysOn.ApplicationExceptionElement](vpn/alwayson-data.dictionary/applicationexceptionelement.md)
  The dictionary that defines which applications can have traffic outside the VPN tunnel.
- [object VPN.AlwaysOn.TunnelConfigurationElement](vpn/alwayson-data.dictionary/tunnelconfigurationelement.md)
  The dictionary used to configure VPN tunnels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/alwayson-data.dictionary/serviceexceptionelement)*