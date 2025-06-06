# init(name:address:port:)

**Framework**: Core MIDI  
**Kind**: init

Creates a host with the specified name, adress, and port.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, address: String, port: Int)
```

## Parameters

- `name`: The host name.
- `address`: The host’s IP address or hostname.
- `port`: The host’s UDP port.

## See Also

- [convenience init(name: String, netService: NetService)](midinetworkhost/init(name:netservice:).md)
  Creates a host with the specified name and net service.
- [convenience init(name: String, netServiceName: String, netServiceDomain: String)](midinetworkhost/init(name:netservicename:netservicedomain:).md)
  Creates a host with the specified name, net service name, and domain.
- [let MIDINetworkBonjourServiceType: String](midinetworkbonjourservicetype.md)
  The Bonjour service type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworkhost/init(name:address:port:))*