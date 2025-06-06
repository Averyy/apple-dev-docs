# uuid

**Framework**: Core Location  
**Kind**: property

The UUID that the observed beacon transmitted.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var uuid: UUID { get }
```

## Mentions

- [Determining the proximity to an iBeacon device](determining-the-proximity-to-an-ibeacon-device.md)

#### Discussion

The UUID is the most significant beacon identity characteristic.  Multiple beacon can transmit the same UUID.

## See Also

- [var major: NSNumber](clbeacon/major.md)
  The major value that the observed beacon transmitted.
- [var minor: NSNumber](clbeacon/minor.md)
  The minor value that the observed beacon transmitted.
- [var proximityUUID: UUID](clbeacon/proximityuuid.md)
  The proximity ID of the beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeacon/uuid)*