# kSCNetworkFlagsReachable

**Framework**: System Configuration  
**Kind**: var

The specified node name or address can be reached using the current network configuration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kSCNetworkFlagsReachable: Int { get }
```

## See Also

- [var kSCNetworkFlagsTransientConnection: Int](kscnetworkflagstransientconnection.md)
  The specified node name or address can be reached via a transient connection, such as PPP.
- [var kSCNetworkFlagsConnectionRequired: Int](kscnetworkflagsconnectionrequired.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established.
- [var kSCNetworkFlagsConnectionAutomatic: Int](kscnetworkflagsconnectionautomatic.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established.
- [var kSCNetworkFlagsInterventionRequired: Int](kscnetworkflagsinterventionrequired.md)
  The specified node name or address can be reached using the current network configuration, but a connection must first be established.
- [var kSCNetworkFlagsIsLocalAddress: Int](kscnetworkflagsislocaladdress.md)
  The specified node name or address is one associated with a network interface on the current system.
- [var kSCNetworkFlagsIsDirect: Int](kscnetworkflagsisdirect.md)
  Network traffic to the specified node name or address does not go through a gateway, but is routed directly to one of the interfaces in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscnetworkflagsreachable)*