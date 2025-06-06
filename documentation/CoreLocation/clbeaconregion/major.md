# major

**Framework**: Core Location  
**Kind**: property

The major value from the beacon identity constraint that defines the beacon region.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@NSCopying
var major: NSNumber? { get }
```

#### Discussion

If you don’t specify a [`major`](clbeaconidentityconstraint/major.md) value for the beacon, the value of this property is `nil`. Operations that compare a beacon’s identity characteristics with the constraint’s characteristics ignore the `major` value if this property is `nil`.

## See Also

- [var uuid: UUID](clbeaconregion/uuid.md)
  The UUID value from the beacon identity constraint that defines the beacon region.
- [var minor: NSNumber?](clbeaconregion/minor.md)
  The minor value from the beacon identity constraint that defines the beacon region.
- [var beaconIdentityConstraint: CLBeaconIdentityConstraint](clbeaconregion/beaconidentityconstraint.md)
  The beacon identity constraint that defines the beacon region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconregion/major)*