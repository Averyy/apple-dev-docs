# registerForConnectionEvents(options:)

**Framework**: Core Bluetooth  
**Kind**: method

Register for an event notification when the central manager makes a connection matching the given options.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func registerForConnectionEvents(options: [CBConnectionEventMatchingOption : Any]? = nil)
```

#### Discussion

When the central manager makes a connection that matches the options, it calls the delegate’s [`centralManager(_:connectionEventDidOccur:for:)`](cbcentralmanagerdelegate/centralmanager(_:connectioneventdidoccur:for:).md) method.

## Parameters

- `options`: A dictionary that specifies options for connection events. See   for a list of possible options.

## See Also

- [Peripheral Connection Options](peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [enum CBConnectionEvent](cbconnectionevent.md)
  A change to the connection state of a peer.
- [struct CBConnectionEventMatchingOption](cbconnectioneventmatchingoption.md)
  A set of options to use when registering for connection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/registerforconnectionevents(options:))*