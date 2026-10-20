# gravity

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The gravity acceleration vector expressed in the device’s reference frame.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var gravity: CMAcceleration { get }
```

```objc
@property (nonatomic, readonly) CMAcceleration gravity;
```

#### Discussion

The total acceleration of the device is equal to gravity plus the acceleration the user imparts to the device ([`userAcceleration`](./useracceleration.md)).

## See Also

### Getting Acceleration Data
- [var userAcceleration: CMAcceleration](./useracceleration.md)
  The acceleration that the user is giving to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/gravity)*