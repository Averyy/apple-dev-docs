# accessories

**Framework**: UIKit  
**Kind**: property

An array of the accessories that decorate the cell.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var accessories: [UICellAccessory] { get set }
```

#### Discussion

System accessories have system-defined placement within the cell. The system automatically determines their rendering order and which side of the cell they appear on. The order of system accessories in the array doesn’t affect their placement.

For custom accessories, you determine their placement. The order of custom accessories in the array affects the order in which the system evaluates their [`UICellAccessory.Placement.Position`](uicellaccessory-swift.struct/placement/position.md).

> ❗ **Important**:  The system throws an exception if you include more than one instance of any system accessory. You can include multiple custom accessories.

## See Also

- [struct UICellAccessory](uicellaccessory-swift.struct.md)
  An accessory in a collection view list cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlistcell/accessories-8nui4)*