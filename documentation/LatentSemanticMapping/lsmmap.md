# LSMMap

**Framework**: Latent Semantic Mapping  
**Kind**: class  
**Role**: Class

A map between a set of categories and related text.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class LSMMap
```

```c
typedef struct __LSMMap * LSMMapRef;
```

## Overview

An [`LSMMap`](./lsmmap.md) is a mutable, opaque Core Foundation type that represents a map.

## Topics

### Creating a Map
- [func LSMMapCreate(CFAllocator?, CFOptionFlags) -> Unmanaged<LSMMap>](./lsmmapcreate%28_,_%29.md)
  Creates a new Latent Semantic Mapping map.
- [Map Flags](./map-flags.md)
  Options for creating a map.
### Managing a Map’s Properties
- [func LSMMapSetProperties(LSMMap, CFDictionary)](./lsmmapsetproperties%28_,_%29.md)
  Sets a dictionary of properties for the map.
- [func LSMMapGetProperties(LSMMap) -> Unmanaged<CFDictionary>](./lsmmapgetproperties%28_%29.md)
  Gets a dictionary of properties for the map.
- [Map Properties](./map-properties.md)
  Special properties that determine a map’s behavior.
### Starting Training Mode
- [func LSMMapStartTraining(LSMMap) -> OSStatus](./lsmmapstarttraining%28_%29.md)
  Puts the map into training mode, preparing it for the addition of more categories or texts.
- [func LSMMapAddCategory(LSMMap) -> LSMCategory](./lsmmapaddcategory%28_%29.md)
  Adds another category and returns its category identifier.
- [func LSMMapGetCategoryCount(LSMMap) -> CFIndex](./lsmmapgetcategorycount%28_%29.md)
  Returns the number of categories in the map.
- [func LSMMapSetStopWords(LSMMap, LSMText) -> OSStatus](./lsmmapsetstopwords%28_,_%29.md)
  Specifies which words to omit from all classification efforts.
- [func LSMMapAddText(LSMMap, LSMText, LSMCategory) -> OSStatus](./lsmmapaddtext%28_,_,_%29.md)
  Adds a training text to the specified category.
- [func LSMMapAddTextWithWeight(LSMMap, LSMText, LSMCategory, Float) -> OSStatus](./lsmmapaddtextwithweight%28_,_,_,_%29.md)
  Adds a training text to the specified category with a weight other than 1.
- [typealias LSMCategory](./lsmcategory.md)
  An integral type that represents a category.
### Starting Classification Mode
- [func LSMMapCompile(LSMMap) -> OSStatus](./lsmmapcompile%28_%29.md)
  Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.
- [func LSMMapCreateClusters(CFAllocator?, LSMMap, CFArray?, CFIndex, CFOptionFlags) -> Unmanaged<CFArray>?](./lsmmapcreateclusters%28_,_,_,_,_%29.md)
  Computes a set of clusters that group similar categories or words.
- [Clustering Flags](./clustering-flags.md)
  Options for creating clusters.
- [func LSMMapApplyClusters(LSMMap, CFArray) -> OSStatus](./lsmmapapplyclusters%28_,_%29.md)
  Groups categories or words (tokens) into the specified sets of clusters.
### Loading and Saving a Map
- [func LSMMapCreateFromURL(CFAllocator?, CFURL, CFOptionFlags) -> Unmanaged<LSMMap>?](./lsmmapcreatefromurl%28_,_,_%29.md)
  Loads a map from the specified file.
- [func LSMMapWriteToURL(LSMMap, CFURL, CFOptionFlags) -> OSStatus](./lsmmapwritetourl%28_,_,_%29.md)
  Compiles the map, if necessary, and stores it into the specified file.
- [func LSMMapWriteToStream(LSMMap, LSMText?, CFWriteStream, CFOptionFlags) -> OSStatus](./lsmmapwritetostream%28_,_,_,_%29.md)
  Writes information about a map or text to a stream in text form.
- [Storage Flags](./storage-flags.md)
  Options for loading and saving a map to a file.
### Getting the Type Identifier
- [func LSMMapGetTypeID() -> CFTypeID](./lsmmapgettypeid%28%29.md)
  Returns the Core Foundation type identifier for Latent Semantic Mapping maps.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Text Classification
- [class LSMText](./lsmtext.md)
  An input text.
- [class LSMResult](./lsmresult.md)
  A result of a lookup in a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmap)*