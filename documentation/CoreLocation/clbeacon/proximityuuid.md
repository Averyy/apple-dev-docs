# proximityUUID

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The proximity ID of the beacon.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.15+ - Deprecated in 10.15

> **Deprecated**: Use [`uuid`](./uuid.md) instead.

## Declaration

```swift
var proximityUUID: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * proximityUUID;
```

## See Also

### Getting the beacon identity
- [var uuid: UUID](./uuid.md)
  The UUID that the observed beacon transmitted.
- [var major: NSNumber](./major.md)
  The major value that the observed beacon transmitted.
- [var minor: NSNumber](./minor.md)
  The minor value that the observed beacon transmitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeacon/proximityuuid)*