# LSMMapSetStopWords(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Specifies which words to omit from all classification efforts.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapSetStopWords(_ mapref: LSMMap, _ textref: LSMText) -> OSStatus
```

#### Discussion

You must call this function before creating any other texts. The `textref` is no longer needed after this call.

## See Also

- [func LSMMapStartTraining(LSMMap) -> OSStatus](lsmmapstarttraining(_:).md)
  Puts the map into training mode, preparing it for the addition of more categories or texts.
- [func LSMMapAddCategory(LSMMap) -> LSMCategory](lsmmapaddcategory(_:).md)
  Adds another category and returns its category identifier.
- [func LSMMapGetCategoryCount(LSMMap) -> CFIndex](lsmmapgetcategorycount(_:).md)
  Returns the number of categories in the map.
- [func LSMMapAddText(LSMMap, LSMText, LSMCategory) -> OSStatus](lsmmapaddtext(_:_:_:).md)
  Adds a training text to the specified category.
- [func LSMMapAddTextWithWeight(LSMMap, LSMText, LSMCategory, Float) -> OSStatus](lsmmapaddtextwithweight(_:_:_:_:).md)
  Adds a training text to the specified category with a weight other than 1.
- [typealias LSMCategory](lsmcategory.md)
  An integral type that represents a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapsetstopwords(_:_:))*