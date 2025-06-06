# connectionOnTraffic

**Framework**: System Configuration  
**Kind**: property

The specified node name or address can be reached using the current network configuration, but a connection must first be established. Any traffic directed to the specified name or address will initiate the connection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var connectionOnTraffic: SCNetworkReachabilityFlags { get }
```

#### Discussion

This flag was previously named `kSCNetworkReachabilityFlagsConnectionAutomatic`.

## See Also

- [static var transientConnection: SCNetworkReachabilityFlags](scnetworkreachabilityflags/transientconnection.md)
  The specified node name or address can be reached via a transient connection, such as PPP.
- [static var reachable: SCNetworkReachabilityFlags](scnetworkreachabilityflags/reachable.md)
  The specified node name or address can be reached using the current network configuration.
- [static var connectionRequired: SCNetworkReachabilityFlags](scnetworkreachabilityflags/connectionrequired.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established. If this flag is set, the `kSCNetworkReachabilityFlagsConnectionOnTraffic` flag, `kSCNetworkReachabilityFlagsConnectionOnDemand` flag, or `kSCNetworkReachabilityFlagsIsWWAN` flag is also typically set to indicate the type of connection required. If the user must manually make the connection, the `kSCNetworkReachabilityFlagsInterventionRequired` flag is also set.
- [static var interventionRequired: SCNetworkReachabilityFlags](scnetworkreachabilityflags/interventionrequired.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established.
- [static var connectionOnDemand: SCNetworkReachabilityFlags](scnetworkreachabilityflags/connectionondemand.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established.
- [static var isLocalAddress: SCNetworkReachabilityFlags](scnetworkreachabilityflags/islocaladdress.md)
  The specified node name or address is one that is associated with a network interface on the current system.
- [static var isDirect: SCNetworkReachabilityFlags](scnetworkreachabilityflags/isdirect.md)
  Network traffic to the specified node name or address will not go through a gateway, but is routed directly to one of the interfaces in the system.
- [static var isWWAN: SCNetworkReachabilityFlags](scnetworkreachabilityflags/iswwan.md)
  The specified node name or address can be reached via a cellular connection, such as EDGE or GPRS.
- [static var connectionAutomatic: SCNetworkReachabilityFlags](scnetworkreachabilityflags/connectionautomatic.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established. Any traffic directed to the specified name or address will initiate the connection. This flag is a synonym for [`connectionOnTraffic`](scnetworkreachabilityflags/connectionontraffic.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/connectionontraffic)*