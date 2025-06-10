# SCNetworkConnectionStatus

**Framework**: System Configuration  
**Kind**: enum

The current status of the network connection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum SCNetworkConnectionStatus
```

#### Overview

This status is intended to be generic and high level. An extended status, specific to the type of network connection, is also available for applications that need additonal information.

## Topics

### Constants
- [SCNetworkConnectionStatus.invalid](scnetworkconnectionstatus/invalid.md)
  The network connection refers to an invalid service.
- [SCNetworkConnectionStatus.disconnected](scnetworkconnectionstatus/disconnected.md)
  The network connection is disconnected.
- [SCNetworkConnectionStatus.connecting](scnetworkconnectionstatus/connecting.md)
  The network connection is connecting.
- [SCNetworkConnectionStatus.connected](scnetworkconnectionstatus/connected.md)
  The network connection is connected.
- [SCNetworkConnectionStatus.disconnecting](scnetworkconnectionstatus/disconnecting.md)
  The network connection is disconnecting.
### Initializers
- [init?(rawValue: Int32)](scnetworkconnectionstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum SCNetworkConnectionPPPStatus](scnetworkconnectionpppstatus.md)
  The PPP-specific status of the network connection.
- [Statistics Dictionary Keys](statistics-dictionary-keys.md)
  Keys associated with values in the statistics dictionary.
- [Selection Options Dictionary Keys](selection-options-dictionary-keys.md)
  Keys used with the [`SCNetworkConnectionCopyUserPreferences(_:_:_:)`](scnetworkconnectioncopyuserpreferences(_:_:_:).md) selection options dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scnetworkconnectionstatus)*