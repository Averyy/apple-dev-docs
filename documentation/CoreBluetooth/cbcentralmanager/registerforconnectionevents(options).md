# registerForConnectionEvents(options:)

**Framework**: Core Bluetooth  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) registerForConnectionEventsWithOptions:(NSDictionary<NSString *,id> *) options;
```

## Discussion

When the central manager makes a connection that matches the options, it calls the delegate’s [`centralManager(_:connectionEventDidOccur:for:)`](../cbcentralmanagerdelegate/centralmanager%28_,connectioneventdidoccur,for%29.md) method.

## Parameters

- `options`: A dictionary that specifies options for connection events. See [Peripheral Connection Options](../peripheral-connection-options.md) for a list of possible options.

## See Also

### Receiving Connection Events
- [Peripheral Connection Options](../peripheral-connection-options.md)
  Keys used to pass options when connecting to a peripheral.
- [enum CBConnectionEvent](../cbconnectionevent.md)
  A change to the connection state of a peer.
- [struct CBConnectionEventMatchingOption](../cbconnectioneventmatchingoption.md)
  A set of options to use when registering for connection events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbcentralmanager/registerforconnectionevents(options:))*