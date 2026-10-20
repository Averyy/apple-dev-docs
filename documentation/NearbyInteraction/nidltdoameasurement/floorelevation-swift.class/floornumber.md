# floorNumber

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

The floor number on which the anchor resides.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var floorNumber: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger floorNumber;
```

#### Discussion

This property indicates the floor that the DL-TDOA anchor is on. Negative values represent floors below ground level.

Use this property in combination with [`height`](./height.md) to determine the precise vertical position of the anchor within a floor, for deployments in buildings that have multiple floors.

## See Also

### Accessing floor elevation components
- [var height: Double](./height.md)
  The height above the floor in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/floorelevation-swift.class/floornumber)*