# attitude

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The attitude of the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var attitude: CMAttitude { get }
```

```objc
@property (nonatomic, readonly) CMAttitude * attitude;
```

#### Discussion

A [`CMAttitude`](../cmattitude.md) object represents a measurement of attitude—that is, the orientation of a body relative to a given frame of reference.

## See Also

### Related Documentation
- [Event Handling Guide for UIKit Apps](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/index.html?language=swift#//apple_ref/doc/uid/TP40009541)
### Getting Attitude and Rotation Rate
- [var rotationRate: CMRotationRate](./rotationrate.md)
  The rotation rate of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/attitude)*