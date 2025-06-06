# MIDINetworkHost

**Framework**: Core MIDI  
**Kind**: class

An object that represents the host’s network address.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MIDINetworkHost
```

## Topics

### Creating Network Hosts
- [convenience init(name: String, address: String, port: Int)](midinetworkhost/init(name:address:port:).md)
  Creates a host with the specified name, adress, and port.
- [convenience init(name: String, netService: NetService)](midinetworkhost/init(name:netservice:).md)
  Creates a host with the specified name and net service.
- [convenience init(name: String, netServiceName: String, netServiceDomain: String)](midinetworkhost/init(name:netservicename:netservicedomain:).md)
  Creates a host with the specified name, net service name, and domain.
- [let MIDINetworkBonjourServiceType: String](midinetworkbonjourservicetype.md)
  The Bonjour service type.
### Inspecting Host Properties
- [var name: String](midinetworkhost/name.md)
  The host name.
- [var netServiceName: String?](midinetworkhost/netservicename.md)
  The net service name.
- [var netServiceDomain: String?](midinetworkhost/netservicedomain.md)
  The net service domain.
- [var address: String](midinetworkhost/address.md)
  The host address.
- [var port: Int](midinetworkhost/port.md)
  The host port.
### Comparing Hosts
- [func hasSameAddress(as: MIDINetworkHost) -> Bool](midinetworkhost/hassameaddress(as:).md)
  Compares this host instance with another to see if they share the same address value.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MIDINetworkConnection](midinetworkconnection.md)
  An object that connects a session to a host.
- [class MIDINetworkSession](midinetworksession.md)
  An object that represents a pairing of a source and destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworkhost)*