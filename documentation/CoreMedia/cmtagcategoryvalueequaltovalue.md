# CMTagCategoryValueEqualToValue

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Compares two tags’s values for equality.

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
static Boolean CMTagCategoryValueEqualToValue(CMTag tag1, CMTag tag2);
```

#### Discussion

This comparison doesn’t take tag data type into account and checks only for equality of the underlying raw 64-bit value.

## See Also

### Comparison and Equality
- [CMTagEqualToTag](./cmtagequaltotag.md)
  Compares two tags for strict equality.
- [CMTagCompare](./cmtagcompare.md)
  Compares two tags in terms of partial equality.
- [CMTagCategoryEqualToTagCategory](./cmtagcategoryequaltotagcategory.md)
  Compares two tags’s categories for equality.
- [CMTagHash](./cmtaghash.md)
  Generates a hash identifier for a tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcategoryvalueequaltovalue)*