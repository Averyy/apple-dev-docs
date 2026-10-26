# reservedLayoutWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout width that the system reserves for the accessory and then centers the accessory within.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) CGFloat reservedLayoutWidth;
```

#### Discussion

Use this property to ensure consistent horizontal alignment from both system and custom accessories to your content, even when the accessories vary in size.

The reserved layout width only affects the amount of space for the accessory, and its positioning within that space. It doesn’t affect the size of the accessory.

![Diagram of three cells, each of which contains one accessory on the leading side. The accessories vary in width, but use the same reserved layout width to achieve consistent alignment. Annotations running the height of the diagram illustrate the static width.](https://developer.apple.com/tutorials/images/com.apple.uikit/media-3680733@2x.png)

## See Also

### Customizing layout and placement
- [UICellAccessoryStandardDimension](../uicellaccessorystandarddimension.md)
  The system standard layout dimension for accessories.
- [UICellAccessoryPlacement](../uicellaccessoryplacement.md)
  Constants that describe the placement of the accessory within the cell.
- [UICellAccessoryPosition](../uicellaccessoryposition.md)
  The index position of the cell accessory in relation to the other accessories in the specified array.
- [UICellAccessoryPositionAfterAccessoryOfClass](../uicellaccessorypositionafteraccessoryofclass.md)
  Provides a position after the accessory that matches the specified class, or at the end if there’s no matching class.
- [UICellAccessoryPositionBeforeAccessoryOfClass](../uicellaccessorypositionbeforeaccessoryofclass.md)
  Provides a position before the accessory that matches the specified class, or at the beginning if there’s no matching class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicellaccessory-c.class/reservedlayoutwidth)*