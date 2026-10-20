# VPN.AlwaysOn.ApplicationExceptionElement

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary that defines which applications can have traffic outside the VPN tunnel.

**Availability**:
- iOS 13.6+
- iPadOS 13.6+
- Mac Catalyst 13.6+
- visionOS 1.0+

## Declaration

```
object VPN.AlwaysOn.ApplicationExceptionElement
```

## Properties

- `BundleIdentifier` (string) *(required)*: The app’s bundle identifier.
- `LimitToProtocols` ([string]): Limit the exception to only the specified list of protocols, with support for `UDP` only.

  **Allowed Values**: `UDP`

## See Also

### Objects
- [object VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement](./allowedcaptivenetworkpluginelement.md)
  The dictionary for captive network configurations.
- [object VPN.AlwaysOn.ServiceExceptionElement](./serviceexceptionelement.md)
  The dictionary that defines service exceptions.
- [object VPN.AlwaysOn.TunnelConfigurationElement](./tunnelconfigurationelement.md)
  The dictionary used to configure VPN tunnels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/alwayson-data.dictionary/applicationexceptionelement)*