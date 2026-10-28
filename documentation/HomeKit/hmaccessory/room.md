# room

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The room containing the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var room: HMRoom? { get }
```

```objc
@property (nonatomic, weak, readonly) HMRoom * room;
```

## Discussion

Assign accessories to new rooms using [`assignAccessory(_:to:completionHandler:)`](../hmhome/assignaccessory%28_,to,completionhandler%29.md).

## See Also

### Locating an accessory
- [class HMRoom](../hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/room)*