# connectionOnDemand

**Framework**: System Configuration  
**Kind**: property  
**Role**: Type Property

The specified node name or address can be reached using the current network configuration, but a connection must first be established.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var connectionOnDemand: SCNetworkReachabilityFlags { get }
```

```c
kSCNetworkReachabilityFlagsConnectionOnDemand
```

## Discussion

The connection will be established “On Demand” by the `CFSocketStream` programming interface (see CFStream Socket Additions for information on this). Other functions will not establish the connection.

## See Also

### Constants
- [static var transientConnection: SCNetworkReachabilityFlags](./transientconnection.md)
  The specified node name or address can be reached via a transient connection, such as PPP.
- [static var reachable: SCNetworkReachabilityFlags](./reachable.md)
  The specified node name or address can be reached using the current network configuration.
- [static var connectionRequired: SCNetworkReachabilityFlags](./connectionrequired.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established. If this flag is set, the `kSCNetworkReachabilityFlagsConnectionOnTraffic` flag, `kSCNetworkReachabilityFlagsConnectionOnDemand` flag, or `kSCNetworkReachabilityFlagsIsWWAN` flag is also typically set to indicate the type of connection required. If the user must manually make the connection, the `kSCNetworkReachabilityFlagsInterventionRequired` flag is also set.
- [static var connectionOnTraffic: SCNetworkReachabilityFlags](./connectionontraffic.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established. Any traffic directed to the specified name or address will initiate the connection.
- [static var interventionRequired: SCNetworkReachabilityFlags](./interventionrequired.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established.
- [static var isLocalAddress: SCNetworkReachabilityFlags](./islocaladdress.md)
  The specified node name or address is one that is associated with a network interface on the current system.
- [static var isDirect: SCNetworkReachabilityFlags](./isdirect.md)
  Network traffic to the specified node name or address will not go through a gateway, but is routed directly to one of the interfaces in the system.
- [static var isWWAN: SCNetworkReachabilityFlags](./iswwan.md)
  The specified node name or address can be reached via a cellular connection, such as EDGE or GPRS.
- [static var connectionAutomatic: SCNetworkReachabilityFlags](./connectionautomatic.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established. Any traffic directed to the specified name or address will initiate the connection. This flag is a synonym for [`connectionOnTraffic`](./connectionontraffic.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkreachabilityflags/connectionondemand)*