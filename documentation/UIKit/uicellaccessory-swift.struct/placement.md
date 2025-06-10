# UICellAccessory.Placement

**Framework**: UIKit  
**Kind**: enum

Constants that describe the placement of the accessory within the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
enum Placement
```

## Topics

### Specifying accessory placement
- [case leading(displayed: UICellAccessory.DisplayedState, at: UICellAccessory.Placement.Position)](uicellaccessory-swift.struct/placement/leading(displayed:at:).md)
  The accessory appears on the leading edge of the cell.
- [case trailing(displayed: UICellAccessory.DisplayedState, at: UICellAccessory.Placement.Position)](uicellaccessory-swift.struct/placement/trailing(displayed:at:).md)
  The accessory appears on the trailing edge of the cell.
### Specifying position
- [static func position(after: UICellAccessory) -> UICellAccessory.Placement.Position](uicellaccessory-swift.struct/placement/position(after:).md)
  Provides a position after the accessory that matches the specified type, or at the end if there’s no matching type.
- [static func position(before: UICellAccessory) -> UICellAccessory.Placement.Position](uicellaccessory-swift.struct/placement/position(before:).md)
  Provides a position before the accessory that matches the specified type, or at the beginning if there’s no matching type.
- [UICellAccessory.Placement.Position](uicellaccessory-swift.struct/placement/position.md)
  The index position of the cell accessory in relation to the other accessories in the specified array.

## See Also

- [UICellAccessory.LayoutDimension](uicellaccessory-swift.struct/layoutdimension.md)
  Constants that describe the layout dimension for the accessory.
- [UICellAccessory.DisplayedState](uicellaccessory-swift.struct/displayedstate.md)
  Constants that describe the cell-editing states that the accessory appears in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-swift.struct/placement)*