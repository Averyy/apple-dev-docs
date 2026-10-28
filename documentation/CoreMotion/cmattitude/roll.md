# roll

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The roll of the device, in radians.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var roll: Double { get }
```

```objc
@property (nonatomic, readonly) double roll;
```

## Mentions

- [Getting processed device-motion data](../getting-processed-device-motion-data.md)

## Discussion

A roll is a rotation around a longitudinal axis that passes through the device from its top to bottom.

## See Also

### Related Documentation
- [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)
### Getting a Mathematical Representation of Attitude as Euler Angles
- [var pitch: Double](./pitch.md)
  The pitch of the device, in radians.
- [var yaw: Double](./yaw.md)
  The yaw of the device, in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmattitude/roll)*