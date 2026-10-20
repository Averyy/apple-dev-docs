# CWInterface

**Framework**: Core WLAN  
**Kind**: class  
**Role**: Class

Encapsulates an IEEE 802.11 interface.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class CWInterface
```

```objc
@interface CWInterface : NSObject
```

#### Overview

Provides access to various WLAN interface parameters, and operations such as scanning for networks, association, and creating computer-to-computer (ad-hoc) networks.

> ❗ **Important**:  Do not instantiate interface objects directly. Instead, use interface objects vended by a [`CWWiFiClient`](./cwwificlient.md) instance via the [`interface()`](./cwwificlient/interface%28%29.md) method or one of its relatives. This enables your app to adopt App Sandbox even when it uses CoreWLAN without the need for any special exceptions. Directly instantiating interface objects causes low level access to system sockets, which by default is not allowed in a sandboxed environment.

## Topics

### Setting interface parameters
- [func setPairwiseMasterKey(Data?) throws](./cwinterface/setpairwisemasterkey%28_%29.md)
  Sets the interface pairwise primary key (PMK).
- [func setPower(Bool) throws](./cwinterface/setpower%28_%29.md)
  Sets the interface power state.
- [func setWEPKey(Data?, flags: CWCipherKeyFlags, index: Int) throws](./cwinterface/setwepkey%28_,flags,index%29.md)
  Sets the interface WEP key.
- [func setWLANChannel(CWChannel) throws](./cwinterface/setwlanchannel%28_%29.md)
  Sets the interface channel.
### Scanning for networks
- [func scanForNetworks(withName: String?) throws -> Set<CWNetwork>](./cwinterface/scanfornetworks%28withname%29.md)
  Scans for networks.
- [func scanForNetworks(withSSID: Data?) throws -> Set<CWNetwork>](./cwinterface/scanfornetworks%28withssid%29.md)
  Scans for networks.
### Getting an interface
- [init(interfaceName: String?)](./cwinterface/init%28interfacename%29.md)
  Convenience method for getting an CWInterface object with the specified name.
- [convenience init(name: String?)](./cwinterface/init%28name%29.md)
  An instance method for obtaining an CWInterface object.
### Getting all attached interfaces
- [class func interfaceNames() -> Set<String>?](./cwinterface/interfacenames%28%29.md)
  Returns the list of BSD names for WLAN interfaces available on the current system.
### Disassociating from a network
- [func disassociate()](./cwinterface/disassociate%28%29.md)
  Disassociates from the current network.
### Creating computer-to-computer networks
- [func startIBSSMode(withSSID: Data, security: CWIBSSModeSecurity, channel: Int, password: String?) throws](./cwinterface/startibssmode%28withssid,security,channel,password%29.md)
  Creates a computer-to-computer (ad-hoc) network with the given network name, security type, and password on the specified channel.
### Committing a configuration
- [func commitConfiguration(CWConfiguration, authorization: SFAuthorization?) throws](./cwinterface/commitconfiguration%28_,authorization%29.md)
  Commit a configuration for the given WLAN interface.
### Associating to a network
- [func associate(toEnterpriseNetwork: CWNetwork, identity: SecIdentity?, username: String?, password: String?) throws](./cwinterface/associate%28toenterprisenetwork,identity,username,password%29.md)
  Connects to the given enterprise network.
- [func associate(to: CWNetwork, password: String?) throws](./cwinterface/associate%28to,password%29.md)
  Associates to a given network using the given network passphrase.
### Instance Properties
- [var interfaceName: String?](./cwinterface/interfacename.md)
  The BSD name of the interface.
### Instance Methods
- [func activePHYMode() -> CWPHYMode](./cwinterface/activephymode%28%29.md)
  The current active PHY modes for the interface.
- [func bssid() -> String?](./cwinterface/bssid%28%29.md)
  The current basic service set identifier (BSSID) for the interface, returned as a UTF-8 string.
- [func cachedScanResults() -> Set<CWNetwork>?](./cwinterface/cachedscanresults%28%29.md)
  The networks currently in the scan cache for the WLAN interface.
- [func configuration() -> CWConfiguration?](./cwinterface/configuration%28%29.md)
  The current configuration for the given WLAN interface.
- [func countryCode() -> String?](./cwinterface/countrycode%28%29.md)
  The current country code (ISO/IEC 3166-1:1997) for the interface.
- [func hardwareAddress() -> String?](./cwinterface/hardwareaddress%28%29.md)
  The hardware media access control (MAC) address for the interface, returned as a UTF-8 string.
- [func interfaceMode() -> CWInterfaceMode](./cwinterface/interfacemode%28%29.md)
  The current mode for the interface.
- [func noiseMeasurement() -> Int](./cwinterface/noisemeasurement%28%29.md)
  The current aggregate noise measurement (dBm) for the interface.
- [func powerOn() -> Bool](./cwinterface/poweron%28%29.md)
  The interface power state is set to “ON”.
- [func rssiValue() -> Int](./cwinterface/rssivalue%28%29.md)
  The current aggregate received signal strength indication (RSSI) measurement (dBm) for the interface.
- [func scanForNetworks(withName: String?, includeHidden: Bool) throws -> Set<CWNetwork>](./cwinterface/scanfornetworks%28withname,includehidden%29.md)
  Scans for networks with the name you specify, optionally including hidden networks.
- [func scanForNetworks(withSSID: Data?, includeHidden: Bool) throws -> Set<CWNetwork>](./cwinterface/scanfornetworks%28withssid,includehidden%29.md)
  Scans for networks with the SSID you specify, optionally including hidden networks.
- [func security() -> CWSecurity](./cwinterface/security%28%29.md)
  The current security mode for the interface.
- [func serviceActive() -> Bool](./cwinterface/serviceactive%28%29.md)
  The interface has its corresponding network service enabled.
- [func ssid() -> String?](./cwinterface/ssid%28%29.md)
  The current service set identifier (SSID) for the interface, encoded as a string.
- [func ssidData() -> Data?](./cwinterface/ssiddata%28%29.md)
  The current service set identifier (SSID) for the interface, returned as data.
- [func supportedWLANChannels() -> Set<CWChannel>?](./cwinterface/supportedwlanchannels%28%29.md)
  An array of channels supported by the interface for the active country code.
- [func transmitPower() -> Int](./cwinterface/transmitpower%28%29.md)
  The current transmit power (mW) for the interface.
- [func transmitRate() -> Double](./cwinterface/transmitrate%28%29.md)
  The current transmit rate (Mbps) for the interface.
- [func wlanChannel() -> CWChannel?](./cwinterface/wlanchannel%28%29.md)
  The current channel for the interface.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class CWChannel](./cwchannel.md)
  Encapsulates an IEEE 802.11 channel.
- [class CWConfiguration](./cwconfiguration.md)
  Encapsulates an immutable configuration for an AirPort WLAN interface.
- [class CWMutableConfiguration](./cwmutableconfiguration.md)
  Encapsulates a mutable configuration for an AirPort WLAN interface.
- [class CWMutableNetworkProfile](./cwmutablenetworkprofile.md)
  Encapsulates a mutable network profile entry.
- [class CWNetwork](./cwnetwork.md)
  Encapsulates an IEEE 802.11 network, providing read-only accessors to various properties of the network.
- [class CWNetworkProfile](./cwnetworkprofile.md)
  Encapsulates an immutable network profile entry.
- [class CWWiFiClient](./cwwificlient.md)
  A wrapper around the entire Wi-Fi subsystem that you use to access interfaces and set up event notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface)*