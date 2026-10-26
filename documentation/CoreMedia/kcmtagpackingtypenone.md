# kCMTagPackingTypeNone

**Framework**: Core Media  
**Kind**: var  
**Role**: Global Variable

A frame-packing tag value for video without packed frames.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
extern const CMTag kCMTagPackingTypeNone;
```

#### Discussion

This value is for use in tags with the [`kCMTagCategory_PackingType`](./cmtagcategory/kcmtagcategory_packingtype.md) category.

## See Also

### Frame Arrangements
- [kCMTagPackingTypeSideBySide](./kcmtagpackingtypesidebyside.md)
  A tag stating that associated video has packed frames with a left eye image on the left and right eye image on the right.
- [kCMTagPackingTypeOverUnder](./kcmtagpackingtypeoverunder.md)
  A tag stating that associated video has packed frames with a left eye image on the top and right eye image on the bottom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtagpackingtypenone)*