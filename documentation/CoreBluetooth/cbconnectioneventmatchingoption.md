# CBConnectionEventMatchingOption

**Framework**: Core Bluetooth  
**Kind**: struct

A set of options to use when registering for connection events.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct CBConnectionEventMatchingOption
```

## Topics

### Creating a Matching Option Instance
- [init(rawValue: String)](cbconnectioneventmatchingoption/init(rawvalue:).md)
  Creates a matching option from the provided raw value.
### Matching Options
- [static let peripheralUUIDs: CBConnectionEventMatchingOption](cbconnectioneventmatchingoption/peripheraluuids.md)
  An array of UUID objects that represents peripherals to match.
- [static let serviceUUIDs: CBConnectionEventMatchingOption](cbconnectioneventmatchingoption/serviceuuids.md)
  An array that represents service identifiers to match.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func registerForConnectionEvents(options: [CBConnectionEventMatchingOption : Any]?)](cbcentralmanager/registerforconnectionevents(options:).md)
  Register for an event notification when the central manager makes a connection matching the given options.
- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [enum CBConnectionEvent](cbconnectionevent.md)
  A change to the connection state of a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbconnectioneventmatchingoption)*