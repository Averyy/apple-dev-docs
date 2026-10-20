# LSMMapGetCategoryCount(_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Returns the number of categories in the map.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapGetCategoryCount(_ mapref: LSMMap) -> CFIndex
```

```c
CFIndex LSMMapGetCategoryCount(LSMMapRef mapref);
```

## See Also

### Starting Training Mode
- [func LSMMapStartTraining(LSMMap) -> OSStatus](./lsmmapstarttraining%28_%29.md)
  Puts the map into training mode, preparing it for the addition of more categories or texts.
- [func LSMMapAddCategory(LSMMap) -> LSMCategory](./lsmmapaddcategory%28_%29.md)
  Adds another category and returns its category identifier.
- [func LSMMapSetStopWords(LSMMap, LSMText) -> OSStatus](./lsmmapsetstopwords%28_,_%29.md)
  Specifies which words to omit from all classification efforts.
- [func LSMMapAddText(LSMMap, LSMText, LSMCategory) -> OSStatus](./lsmmapaddtext%28_,_,_%29.md)
  Adds a training text to the specified category.
- [func LSMMapAddTextWithWeight(LSMMap, LSMText, LSMCategory, Float) -> OSStatus](./lsmmapaddtextwithweight%28_,_,_,_%29.md)
  Adds a training text to the specified category with a weight other than 1.
- [typealias LSMCategory](./lsmcategory.md)
  An integral type that represents a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapgetcategorycount(_:))*