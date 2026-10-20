# major

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The major value that the observed beacon transmitted.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@NSCopying
var major: NSNumber { get }
```

```objc
@property (nonatomic, copy, readonly) NSNumber * major;
```

## Mentions

- [Determining the proximity to an iBeacon device](../determining-the-proximity-to-an-ibeacon-device.md)

## See Also

### Getting the beacon identity
- [var uuid: UUID](./uuid.md)
  The UUID that the observed beacon transmitted.
- [var minor: NSNumber](./minor.md)
  The minor value that the observed beacon transmitted.
- [var proximityUUID: UUID](./proximityuuid.md)
  The proximity ID of the beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeacon/major)*