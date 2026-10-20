# VPN.AlwaysOn.TunnelConfigurationElement

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary used to configure VPN tunnels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```
object VPN.AlwaysOn.TunnelConfigurationElement
```

## Properties

- `Interfaces` ([string]): The interfaces to apply this configuration to.

  **Allowed Values**: `Cellular`, `WiFi`
- `ProtocolType` (string) *(required)*: The type of connection, which needs to be `IKEv2`.

  **Allowed Values**: `IKEv2`

## See Also

### Objects
- [object VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement](./allowedcaptivenetworkpluginelement.md)
  The dictionary for captive network configurations.
- [object VPN.AlwaysOn.ApplicationExceptionElement](./applicationexceptionelement.md)
  The dictionary that defines which applications can have traffic outside the VPN tunnel.
- [object VPN.AlwaysOn.ServiceExceptionElement](./serviceexceptionelement.md)
  The dictionary that defines service exceptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/alwayson-data.dictionary/tunnelconfigurationelement)*