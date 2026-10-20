# VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary for captive network configurations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```
object VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement
```

## Properties

- `BundleIdentifier` (string) *(required)*: The bundle identifier for the app that’s allowed on the captive network.

## See Also

### Objects
- [object VPN.AlwaysOn.ApplicationExceptionElement](./applicationexceptionelement.md)
  The dictionary that defines which applications can have traffic outside the VPN tunnel.
- [object VPN.AlwaysOn.ServiceExceptionElement](./serviceexceptionelement.md)
  The dictionary that defines service exceptions.
- [object VPN.AlwaysOn.TunnelConfigurationElement](./tunnelconfigurationelement.md)
  The dictionary used to configure VPN tunnels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/alwayson-data.dictionary/allowedcaptivenetworkpluginelement)*