# LSMCategory

**Framework**: Latent Semantic Mapping  
**Kind**: typealias

An integral type that represents a category.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias LSMCategory = UInt32
```

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
- [func LSMMapAddTextWithWeight(LSMMap, LSMText, LSMCategory, Float) -> OSStatus](lsmmapaddtextwithweight(_:_:_:_:).md)
  Adds a training text to the specified category with a weight other than 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmcategory)*