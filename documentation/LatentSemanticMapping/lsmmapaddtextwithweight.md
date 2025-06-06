# LSMMapAddTextWithWeight(_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Adds a training text to the specified category with a weight other than 1.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapAddTextWithWeight(_ mapref: LSMMap, _ textref: LSMText, _ category: LSMCategory, _ weight: Float) -> OSStatus
```

#### Discussion

The weight may be negative, but global counts are pinned to `0`. The `textref` is no longer needed after this call.

## See Also

- [func LSMMapStartTraining(LSMMap) -> OSStatus](lsmmapstarttraining(_:).md)
  Puts the map into training mode, preparing it for the addition of more categories or texts.
- [func LSMMapAddCategory(LSMMap) -> LSMCategory](lsmmapaddcategory(_:).md)
  Adds another category and returns its category identifier.
- [func LSMMapGetCategoryCount(LSMMap) -> CFIndex](lsmmapgetcategorycount(_:).md)
  Returns the number of categories in the map.
- [func LSMMapSetStopWords(LSMMap, LSMText) -> OSStatus](lsmmapsetstopwords(_:_:).md)
  Specifies which words to omit from all classification efforts.
- [func LSMMapAddText(LSMMap, LSMText, LSMCategory) -> OSStatus](lsmmapaddtext(_:_:_:).md)
  Adds a training text to the specified category.
- [typealias LSMCategory](lsmcategory.md)
  An integral type that represents a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapaddtextwithweight(_:_:_:_:))*