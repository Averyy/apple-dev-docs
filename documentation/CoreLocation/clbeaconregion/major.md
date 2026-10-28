# major

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The major value from the beacon identity constraint that defines the beacon region.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
@NSCopying
var major: NSNumber? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * major;
```

## Discussion

If you don’t specify a [`major`](../clbeaconidentityconstraint/major.md) value for the beacon, the value of this property is `nil`. Operations that compare a beacon’s identity characteristics with the constraint’s characteristics ignore the `major` value if this property is `nil`.

## See Also

### Getting the beacon identity
- [var uuid: UUID](./uuid.md)
  The UUID value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](./minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](./beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/major)*