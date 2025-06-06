# room

**Framework**: HomeKit  
**Kind**: property

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

#### Discussion

Assign accessories to new rooms using [`assignAccessory(_:to:completionHandler:)`](hmhome/assignaccessory(_:to:completionhandler:).md).

## See Also

- [class HMRoom](hmroom.md)
  The smallest subdivision of a home’s space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/room)*