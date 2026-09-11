# NetworkVPNAlwaysOnTunnelConfigurationElementObject

**Framework**: Device Management  
**Kind**: dictionary

An array that contains an arbitrary number of tunnel configurations.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- visionOS 27.0+

## Declaration

```swift
object NetworkVPNAlwaysOnTunnelConfigurationElementObject
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2Object](networkvpnalwaysontunnelconfigurationelement_ikev2object.md)
  The IKEv2 configuration for this tunnel.

## Properties

- `IKEV2` (NetworkVPNAlwaysOnTunnelConfigurationElement_IKEV2Object): The IKEv2 configuration for this tunnel.
- `Interfaces` ([string]): The interfaces to apply this configuration to.
- `ProtocolType` (string) *(required)*: The type of connection, which needs to be `IKEv2`.

## See Also

- [object NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject](networkvpnalwaysonallowedcaptivenetworkpluginelementobject.md)
  The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- [object NetworkVPNAlwaysOnApplicationExceptionElementObject](networkvpnalwaysonapplicationexceptionelementobject.md)
  An array that contains an arbitrary number of apps whose connections occur outside the VPN.
- [object NetworkVPNAlwaysOnServiceExceptionElementObject](networkvpnalwaysonserviceexceptionelementobject.md)
  An array that contains an arbitrary number of service exceptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysontunnelconfigurationelementobject)*