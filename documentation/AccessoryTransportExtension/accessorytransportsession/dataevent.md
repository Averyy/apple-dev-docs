# AccessoryTransportSession.DataEvent

**Framework**: Accessory Transport Extension  
**Kind**: enum

An enumeration of data events that the transport extension receives.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
enum DataEvent
```

#### Overview

The [`AccessoryTransportSession.EventHandler`](accessorytransportsession/eventhandler.md) protocol’s [`dataEventHandler(event:)`](accessorytransportsession/eventhandler/dataeventhandler(event:).md) method receives events of this type.

## Topics

### Identifying data event types
- [AccessoryTransportSession.DataEvent.plaintext(data:featureID:)](accessorytransportsession/dataevent/plaintext(data:featureid:).md)
  A data event that contains unencrypted data for a feature.
- [AccessoryTransportSession.DataEvent.ciphertext(data:featureID:)](accessorytransportsession/dataevent/ciphertext(data:featureid:).md)
  A data event that contains encrypted data for a specific feature.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [AccessoryTransportSession.EventHandler](accessorytransportsession/eventhandler.md)
  A protocol that defines methods for handling transport session events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/dataevent)*