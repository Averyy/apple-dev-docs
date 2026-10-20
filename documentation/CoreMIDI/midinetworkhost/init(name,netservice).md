# init(name:netService:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a host with the specified name and net service.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
convenience init(name: String, netService: NetService)
```

```objc
+ (instancetype) hostWithName:(NSString *) name netService:(NSNetService *) netService;
```

## Parameters

- `name`: The host name.
- `netService`: The net service.

## See Also

### Creating Network Hosts
- [convenience init(name: String, address: String, port: Int)](./init%28name,address,port%29.md)
  Creates a host with the specified name, adress, and port.
- [convenience init(name: String, netServiceName: String, netServiceDomain: String)](./init%28name,netservicename,netservicedomain%29.md)
  Creates a host with the specified name, net service name, and domain.
- [let MIDINetworkBonjourServiceType: String](../midinetworkbonjourservicetype.md)
  The Bonjour service type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworkhost/init(name:netservice:))*