# pitch

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The pitch of the device, in radians.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var pitch: Double { get }
```

```objc
@property (nonatomic, readonly) double pitch;
```

## Mentions

- [Getting processed device-motion data](../getting-processed-device-motion-data.md)

## Discussion

A pitch is a rotation around a lateral axis that passes through the device from side to side.

## See Also

### Getting a Mathematical Representation of Attitude as Euler Angles
- [var roll: Double](./roll.md)
  The roll of the device, in radians.
- [var yaw: Double](./yaw.md)
  The yaw of the device, in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitude/pitch)*