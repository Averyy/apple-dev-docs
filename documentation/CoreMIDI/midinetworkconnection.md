# MIDINetworkConnection

**Framework**: Core MIDI  
**Kind**: class  
**Role**: Class

An object that connects a session to a host.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MIDINetworkConnection
```

```objc
@interface MIDINetworkConnection : NSObject
```

## Topics

### Creating Connections
- [convenience init(host: MIDINetworkHost)](./midinetworkconnection/init%28host%29.md)
  Creates a connection to the specified host.
### Accessing Connections
- [var host: MIDINetworkHost](./midinetworkconnection/host.md)
  The host connection.

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

### Networking
- [class MIDINetworkHost](./midinetworkhost.md)
  An object that represents the host’s network address.
- [class MIDINetworkSession](./midinetworksession.md)
  An object that represents a pairing of a source and destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midinetworkconnection)*