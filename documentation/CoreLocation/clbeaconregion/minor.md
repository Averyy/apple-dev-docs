# minor

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The minor value from the beacon identity constraint that defines the beacon region.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2

## Declaration

```swift
@NSCopying
var minor: NSNumber? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * minor;
```

#### Discussion

If you don’t specify a `minor` value for the beacon, the value of this property is `nil`. Operations that compare a beacon’s identity characteristics with the constraint’s characteristics ignore the `minor` value if this property is `nil`.

## See Also

### Getting the beacon identity
- [var uuid: UUID](./uuid.md)
  The UUID value from the beacon identity constraint that defines the beacon region.
- [var major: NSNumber?](./major.md)
  The major value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](./beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/minor)*