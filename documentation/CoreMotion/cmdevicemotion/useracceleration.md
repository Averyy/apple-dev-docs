# userAcceleration

**Framework**: Core Motion  
**Kind**: property

The acceleration that the user is giving to the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var userAcceleration: CMAcceleration { get }
```

#### Discussion

The total acceleration of the device is equal to [`gravity`](cmdevicemotion/gravity.md) plus the acceleration the user imparts to the device.

## See Also

- [var gravity: CMAcceleration](cmdevicemotion/gravity.md)
  The gravity acceleration vector expressed in the device’s reference frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/useracceleration)*