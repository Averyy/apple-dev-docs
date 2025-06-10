# NETunnelProviderManager

**Framework**: Network Extension  
**Kind**: class

An object to create and manage the tunnel provider’s VPN configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NETunnelProviderManager
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Overview

Like its superclass [`NEVPNManager`](nevpnmanager.md), you use the [`NETunnelProviderManager`](netunnelprovidermanager.md) class to configure and control VPN connections. The difference is that [`NETunnelProviderManager`](netunnelprovidermanager.md) is used to to configure and control VPN connections that use a custom VPN protocol. The client side of the custom protocol implementation is implemented as a Packet Tunnel Provider extension. The Packet Tunnel Provider extension’s containing app uses [`NETunnelProviderManager`](netunnelprovidermanager.md) to create and manage VPN configurations that use the custom protocol, and to control the VPN connections specified by the configurations.

The [`NETunnelProviderManager`](netunnelprovidermanager.md) class inherits most of its functionality from the [`NEVPNManager`](nevpnmanager.md) class. The key differences to be aware of when using [`NETunnelProviderManager`](netunnelprovidermanager.md) are:

- The [`protocolConfiguration`](nevpnmanager/protocolconfiguration.md) property can only be set to instances of the [`NETunnelProviderProtocol`](netunnelproviderprotocol.md) class
- The [`connection`](nevpnmanager/connection.md) read-only property is set to an instance of the [`NETunnelProviderSession`](netunnelprovidersession.md) class.

> ❗ **Important**:  The `com.apple.developer.networking.networkextension` entitlement is required to use the [`NETunnelProviderManager`](netunnelprovidermanager.md) class. Enable this entitlement when creating an App ID in your developer account.

##### Configuration Model

Each [`NETunnelProviderManager`](netunnelprovidermanager.md) instance corresponds to a single VPN configuration stored in the Network Extension preferences. Multiple VPN configurations can be created and managed by creating multiple [`NETunnelProviderManager`](netunnelprovidermanager.md) instances.

Each VPN configuration is associated with the app that created it. The app’s view of the Network Extension preferences is limited to include only the configurations that were created by the app.

VPN configurations created using [`NETunnelProviderManager`](netunnelprovidermanager.md) are classified as regular enterprise VPN configurations (as opposed to the Personal VPN configurations created by `NEVPNManager`). Only one enterprise VPN configuration can be enabled on the system at a time. If both a Personal VPN and an enterprise VPN are active on the system simultaneously, the enterprise VPN takes precedence, meaning that if the routes for the two VPNs conflict then the routes for the enterprise VPN will take precedence. The Personal VPN will remain active and connected while the enterprise VPN is active and connected, and any traffic that is routed to the Personal VPN and is not routed to the enterprise VPN will continue to traverse the Personal VPN.

##### Profile Configuration

It is possible to create Packet Tunnel Provider configurations using configuration profiles. See the `com.apple.vpn.managed` and `com.apple.vpn.managed.applayer` payload types in [`Configuration Profile Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206). To specify that a configuration created via a profile payload is associated with a particular app (and therefore allow the app to use `NETunnelProviderManager` to manage the configuration), the app’s bundle identifier must be set as the value of the `VPNSubType` field in the profile payload.

Credential Storage

VPN credentials such as private keys and passwords that are imported into the system via configuration profiles are stored in the keychain in a special access group called `com.apple.managed.vpn.shared`. In order to use these credentials the app and Packet Tunnel Provider extension must have the `com.apple.managed.vpn.shared` keychain access group entitlement.

> ❗ **Important**:  The app and Packet Tunnel Provider extension must not write to the `com.apple.managed.vpn.shared` keychain access group. When writing to the keychain, the app and Packet Tunnel Provider must target a different keychain access group.

##### Routing Network Data to the Vpn

There are two ways or methods by which network data is routed to the VPN:

- By destination IP address
- By source application (Per-App VPN)

Routing by Destination IP

This is the default routing method. The IP routes are specified by the Packet Tunnel Provider extension at the time that the VPN tunnel is fully established. See [`NETunnelProvider`](netunnelprovider.md) for more details.

Per-App VPN

The only way to configure Per-App VPN is by enrolling the device in a Mobile Device Management (MDM) system, and then linking apps that are managed by the MDM system with a VPN configuration created from a `com.apple.vpn.managed.applayer` configuration profile payload. Here are some details about how this works:

- The MDM server creates a configuration profile containing a `com.apple.vpn.managed.applayer` payload. The `com.apple.vpn.managed.applayer` payload contains all of the usual VPN configuration profile payload fields, and also must contain a `VPNUUID` field, containing a unique string defined by the MDM server.
- If the VPN provider extension is a Packet Tunnel Provider extension, then the `ProviderType` field in the `com.apple.vpn.managed.applayer` payload should be set to `packet-tunnel`. If the VPN provider extension is an App Proxy Provider extension, then the `ProviderType` field in the `com.apple.vpn.managed.applayer` should be set to `app-proxy`.
- The MDM server adds a `VPNUUID` key to the attributes dictionary of all of the managed apps that will use the VPN. The value of the `VPNUUID` key must be set to the same unique string contained in the `VPNUUID` field in the `com.apple.vpn.managed.applayer` payload.
- The MDM server pushes the configuration profile and the managed apps to the iOS device using the MDM protocol.

The MDM client running on the device creates one app rule in the VPN configuration for each managed app that is linked to the VPN configuration via the `VPNUUID` app attribute.

> **Note**:  It is not possible to create app rules for Apple system apps. The one exception to this rule is Safari. In the case of Safari, the VPN can only tunnel the network traffic for web sites in certain domains, not all web sites. See the `SafariDomains` field in [`Configuration Profile Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).

Per-App VPN On Demand

The Per-App VPN app rules serve as both routing rules and VPN On Demand rules. This is in contrast to IP destination-based routing, where the VPN On Demand rules are configured separately from the routing rules. When the `onDemandEnabled` property is set to [`true`](https://developer.apple.com/documentation/swift/true) and an app that matches the Per-App VPN rules attempts to communicate over the network, the VPN will be started automatically.

It is possible to set regular VPN On Demand rules in a Per-App VPN configuration via the [`onDemandRules`](nevpnmanager/ondemandrules.md) property, but only [`NEOnDemandRuleDisconnect`](neondemandruledisconnect.md) rules will be used. When a `NEOnDemandRuleDisconnect` rule matches, apps which match the Per-App VPN rules will bypass the VPN.

Testing Per-App VPN

As described above, an MDM server is required to configure Per-App VPN for VPN apps distributed via the App Store. To make testing Per-App VPN easier, it is possible to configure Per-App VPN without an MDM server during development by using the `NETestAppMapping` `Info.plist` key.

> ❗ **Important**:  The `NETestAppMapping Info.plist` key can only be used to create app rules in apps that are signed with a Development provisioning profile. In apps that are signed with Distribution provisioning profiles the `NETestAppMapping Info.plist` key has no effect.

Here is what you need to do to make use of this capability:

- Create a configuration profile containing a `com.apple.vpn.managed.applayer` payload as described in [`Configuration Profile Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206). In addition to all of the usual VPN configuration payload fields, the payload must also contain a `VPNUUID` field, containing a unique string defined by you.
- Add the `NETestAppMapping` key to your app’s `Info.plist`. The value of this key should be a dictionary that maps `VPNUUID` values to arrays of app bundle identifiers. Here is a sample:

```xml
  <key>NETestAppMapping</key
  <dict>
      <key>3D7A07D8-97D0-4E5A-BB04-1EB82DD12A35</key>
      <array>
          <string>my.greatenterprise.SuperApp</string>
      </array>
  <dict>
```

- Rebuild the app.
- Install the app and the configuration profile on the device.

The system will create one app rule in the VPN configuration for each bundle identifier listed in the array in the `NETestAppMapping` dictionary corresponding to the value of the `VPNUUID` field in the `com.apple.vpn.managed.applayer` payload.

## Topics

### Managing tunnel configurations
- [class func loadAllFromPreferences(completionHandler: ([NETunnelProviderManager]?, (any Error)?) -> Void)](netunnelprovidermanager/loadallfrompreferences(completionhandler:).md)
  Read all of the VPN configurations created by the calling app that have previously been saved to the Network Extension preferences.
- [func copyAppRules() -> [NEAppRule]?](netunnelprovidermanager/copyapprules.md)
  Returns a copy of the app rules currently set in the configuration.
### Getting tunnel configuration properties
- [var routingMethod: NETunnelProviderRoutingMethod](netunnelprovidermanager/routingmethod.md)
  The method that the system uses to route network traffic to the tunnel.
- [enum NETunnelProviderRoutingMethod](netunnelproviderroutingmethod.md)
### Configuring a per-app VPN
- [class func forPerAppVPN() -> Self](netunnelprovidermanager/forperappvpn.md)
  Returns a tunnel provider manager for managing a per-app VPN configuration.
- [var appRules: [NEAppRule]](netunnelprovidermanager/apprules.md)
  The rules for specific apps in a per-app VPN.
- [var excludedDomains: [String]](netunnelprovidermanager/excludeddomains.md)
  The domains that the system excludes from a per-app VPN.
- [var associatedDomains: [String]](netunnelprovidermanager/associateddomains.md)
  The domains that the system routes network traffic through for a per-app VPN.
- [var calendarDomains: [String]](netunnelprovidermanager/calendardomains.md)
  The calendar servers that the system routes connections from the Calendar app through for a per-app VPN.
- [var contactsDomains: [String]](netunnelprovidermanager/contactsdomains.md)
  The contacts servers that the system routes connections from the Contacts app through for a per-app VPN.
- [var mailDomains: [String]](netunnelprovidermanager/maildomains.md)
  The mail servers that the system routes connections from the Mail app through for a per-app VPN.
- [var safariDomains: [String]](netunnelprovidermanager/safaridomains.md)
  The website domains that the system routes connections from the Safari app through a per-app VPN.

## Relationships

### Inherits From
- [NEVPNManager](nevpnmanager.md)
### Inherited By
- [NEAppProxyProviderManager](neappproxyprovidermanager.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEAppProxyProviderManager](neappproxyprovidermanager.md)
  An object to create and manage the app proxy provider’s VPN configuration.
- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class NETunnelProviderProtocol](netunnelproviderprotocol.md)
  Configuration parameters for a VPN tunnel.
- [class NEAppRule](neapprule.md)
  The identity of an app whose traffic is to be routed through the tunnel.
- [VPN On Demand Rules](vpn-on-demand-rules.md)
  Set up VPN On Demand.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager)*