# height

**Framework**: Nearby Interaction  
**Kind**: property

The height above the floor in meters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var height: Double { get }
```

#### Discussion

This property specifies the vertical distance, in meters, from the floor surface to the DL-TDOA anchor’s location in the environment.

Use this property in combination with [`floorNumber`](nidltdoameasurement/floorelevation-swift.class/floornumber.md) to determine the complete vertical position of the anchor in a multi-story environment.

## See Also

- [var floorNumber: Int](nidltdoameasurement/floorelevation-swift.class/floornumber.md)
  The floor number on which the anchor resides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/floorelevation-swift.class/height)*