# VPN.AlwaysOn

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary that contains IPSec settings.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```
object VPN.AlwaysOn
```

## Topics

### Objects
- [object VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement](./alwayson-data.dictionary/allowedcaptivenetworkpluginelement.md)
  The dictionary for captive network configurations.
- [object VPN.AlwaysOn.ApplicationExceptionElement](./alwayson-data.dictionary/applicationexceptionelement.md)
  The dictionary that defines which applications can have traffic outside the VPN tunnel.
- [object VPN.AlwaysOn.ServiceExceptionElement](./alwayson-data.dictionary/serviceexceptionelement.md)
  The dictionary that defines service exceptions.
- [object VPN.AlwaysOn.TunnelConfigurationElement](./alwayson-data.dictionary/tunnelconfigurationelement.md)
  The dictionary used to configure VPN tunnels.

## Properties

- `AllowAllCaptiveNetworkPlugins` (integer): If `1`, allows traffic from all captive networking apps outside the VPN tunnel to perform captive network handling.

  **Default**: `0`; **Allowed Values**: `0`, `1`
- `AllowCaptiveWebSheet` (integer): If `1`, allows traffic from Captive Web Sheet outside the VPN tunnel.

  **Default**: `0`; **Allowed Values**: `0`, `1`
- `AllowedCaptiveNetworkPlugins` ([VPN.AlwaysOn.AllowedCaptiveNetworkPluginElement]): The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- `ApplicationExceptions` ([VPN.AlwaysOn.ApplicationExceptionElement]): An array that contains an arbitrary number of apps whose connections occur outside the VPN.

  Available: iOS 13.6+ | iPadOS 13.6+ | visionOS 1+
- `ServiceExceptions` ([VPN.AlwaysOn.ServiceExceptionElement]): An array that contains an arbitrary number of service exceptions.
- `TunnelConfigurations` ([VPN.AlwaysOn.TunnelConfigurationElement]) *(required)*: An array that contains an arbitrary number of tunnel configurations.
- `UIToggleEnabled` (integer): If `1`, allows the user to disable the VPN configuration.

  **Default**: `0`; **Allowed Values**: `0`, `1`

## See Also

### Objects
- [object VPN.DNS](./dns-data.dictionary.md)
  The dictionary to configure DNS settings for the VPN.
- [object VPN.IKEv2](./ikev2-data.dictionary.md)
  The dictionary to use for an IKEv2 VPN type.
- [object VPN.IPSec](./ipsec-data.dictionary.md)
  The dictionary to use for an IPSec VPN type.
- [object VPN.IPv4](./ipv4-data.dictionary.md)
  The dictionary that contains IPV4 settings.
- [object VPN.PPP](./ppp-data.dictionary.md)
  The dictionary that contains PPP settings.
- [object VPN.Proxies](./proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.TransparentProxy](./transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](./vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](./vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/alwayson-data.dictionary)*