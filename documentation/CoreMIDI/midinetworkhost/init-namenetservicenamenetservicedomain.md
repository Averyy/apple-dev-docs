# init(name:netServiceName:netServiceDomain:)

**Framework**: Core MIDI  
**Kind**: init

Creates a host with the specified name, net service name, and domain.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, netServiceName: String, netServiceDomain: String)
```

## Parameters

- `name`: The host name.
- `netServiceName`: The net service name.
- `netServiceDomain`: The net service domain.

## See Also

- [convenience init(name: String, address: String, port: Int)](midinetworkhost/init(name:address:port:).md)
  Creates a host with the specified name, adress, and port.
- [convenience init(name: String, netService: NetService)](midinetworkhost/init(name:netservice:).md)
  Creates a host with the specified name and net service.
- [let MIDINetworkBonjourServiceType: String](midinetworkbonjourservicetype.md)
  The Bonjour service type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworkhost/init(name:netservicename:netservicedomain:))*