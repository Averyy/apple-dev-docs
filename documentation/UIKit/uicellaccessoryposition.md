# UICellAccessoryPosition

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

The index position of the cell accessory in relation to the other accessories in the specified array.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
typedef unsigned long (^)(NSArray<__kindof UICellAccessory *> *) UICellAccessoryPosition;
```

## See Also

### Customizing layout and placement
- [reservedLayoutWidth](./uicellaccessory-c.class/reservedlayoutwidth.md)
  The layout width that the system reserves for the accessory and then centers the accessory within.
- [UICellAccessoryStandardDimension](./uicellaccessorystandarddimension.md)
  The system standard layout dimension for accessories.
- [UICellAccessoryPlacement](./uicellaccessoryplacement.md)
  Constants that describe the placement of the accessory within the cell.
- [UICellAccessoryPositionAfterAccessoryOfClass](./uicellaccessorypositionafteraccessoryofclass.md)
  Provides a position after the accessory that matches the specified class, or at the end if there’s no matching class.
- [UICellAccessoryPositionBeforeAccessoryOfClass](./uicellaccessorypositionbeforeaccessoryofclass.md)
  Provides a position before the accessory that matches the specified class, or at the beginning if there’s no matching class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessoryposition)*