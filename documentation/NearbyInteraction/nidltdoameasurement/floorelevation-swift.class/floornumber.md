# floorNumber

**Framework**: Nearby Interaction  
**Kind**: property

The floor number on which the anchor resides.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var floorNumber: Int { get }
```

#### Discussion

This property indicates the floor that the DL-TDOA anchor is on. Negative values represent floors below ground level.

Use this property in combination with [`height`](nidltdoameasurement/floorelevation-swift.class/height.md) to determine the precise vertical position of the anchor within a floor, for deployments in buildings that have multiple floors.

## See Also

- [var height: Double](nidltdoameasurement/floorelevation-swift.class/height.md)
  The height above the floor in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/floorelevation-swift.class/floornumber)*