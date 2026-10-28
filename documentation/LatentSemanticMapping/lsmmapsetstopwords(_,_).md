# LSMMapSetStopWords(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Specifies which words to omit from all classification efforts.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapSetStopWords(_ mapref: LSMMap, _ textref: LSMText) -> OSStatus
```

```c
OSStatus LSMMapSetStopWords(LSMMapRef mapref, LSMTextRef textref);
```

## Discussion

You must call this function before creating any other texts. The `textref` is no longer needed after this call.

## See Also

### Starting Training Mode
- [func LSMMapStartTraining(LSMMap) -> OSStatus](./lsmmapstarttraining%28_%29.md)
  Puts the map into training mode, preparing it for the addition of more categories or texts.
- [func LSMMapAddCategory(LSMMap) -> LSMCategory](./lsmmapaddcategory%28_%29.md)
  Adds another category and returns its category identifier.
- [func LSMMapGetCategoryCount(LSMMap) -> CFIndex](./lsmmapgetcategorycount%28_%29.md)
  Returns the number of categories in the map.
- [func LSMMapAddText(LSMMap, LSMText, LSMCategory) -> OSStatus](./lsmmapaddtext%28_,_,_%29.md)
  Adds a training text to the specified category.
- [func LSMMapAddTextWithWeight(LSMMap, LSMText, LSMCategory, Float) -> OSStatus](./lsmmapaddtextwithweight%28_,_,_,_%29.md)
  Adds a training text to the specified category with a weight other than 1.
- [typealias LSMCategory](./lsmcategory.md)
  An integral type that represents a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapsetstopwords(_:_:))*