# UICellAccessory.Placement.Position

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The index position of the cell accessory in relation to the other accessories in the specified array.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
typealias Position = ([UICellAccessory]) -> Int
```

## See Also

### Specifying position
- [static func position(after: UICellAccessory) -> UICellAccessory.Placement.Position](./position%28after%29.md)
  Provides a position after the accessory that matches the specified type, or at the end if there’s no matching type.
- [static func position(before: UICellAccessory) -> UICellAccessory.Placement.Position](./position%28before%29.md)
  Provides a position before the accessory that matches the specified type, or at the beginning if there’s no matching type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/placement/position)*