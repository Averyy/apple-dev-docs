# init(name:netServiceName:netServiceDomain:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) hostWithName:(NSString *) name netServiceName:(NSString *) netServiceName netServiceDomain:(NSString *) netServiceDomain;
```

## Parameters

- `name`: The host name.
- `netServiceName`: The net service name.
- `netServiceDomain`: The net service domain.

## See Also

### Creating Network Hosts
- [convenience init(name: String, address: String, port: Int)](./init%28name,address,port%29.md)
  Creates a host with the specified name, adress, and port.
- [convenience init(name: String, netService: NetService)](./init%28name,netservice%29.md)
  Creates a host with the specified name and net service.
- [let MIDINetworkBonjourServiceType: String](../midinetworkbonjourservicetype.md)
  The Bonjour service type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworkhost/init(name:netservicename:netservicedomain:))*