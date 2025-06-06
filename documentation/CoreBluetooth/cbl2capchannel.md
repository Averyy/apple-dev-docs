# CBL2CAPChannel

**Framework**: Core Bluetooth  
**Kind**: class

A live L2CAP connection to a remote device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class CBL2CAPChannel
```

## Topics

### Accessing Streams
- [var inputStream: InputStream!](cbl2capchannel/inputstream.md)
  The stream used for reading data from the remote peer.
- [var outputStream: OutputStream!](cbl2capchannel/outputstream.md)
  The stream used for writing data to the peer.
### Accessing the Peer
- [var peer: CBPeer!](cbl2capchannel/peer.md)
  The peer connected to the channel.
### Accessing the Protocol/Service Multiplexer
- [var psm: CBL2CAPPSM](cbl2capchannel/psm.md)
  The PSM of the channel.

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

- [func openL2CAPChannel(CBL2CAPPSM)](cbperipheral/openl2capchannel(_:).md)
  Attempts to open an L2CAP channel to the peripheral using the supplied Protocol/Service Multiplexer (PSM).
- [typealias CBL2CAPPSM](cbl2cappsm.md)
  The type of PSM identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbl2capchannel)*