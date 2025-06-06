# LSMMapCreateClusters(_:_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Computes a set of clusters that group similar categories or words.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapCreateClusters(_ alloc: CFAllocator?, _ mapref: LSMMap, _ subset: CFArray?, _ numClusters: CFIndex, _ flags: CFOptionFlags) -> Unmanaged<CFArray>?
```

#### Discussion

If `subset` is non-`NULL`, this function only performs clustering on the categories or words in `subset`.

## See Also

- [func LSMMapCompile(LSMMap) -> OSStatus](lsmmapcompile(_:).md)
  Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.
- [Clustering Flags](clustering-flags.md)
  Options for creating clusters.
- [func LSMMapApplyClusters(LSMMap, CFArray) -> OSStatus](lsmmapapplyclusters(_:_:).md)
  Groups categories or words (tokens) into the specified sets of clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapcreateclusters(_:_:_:_:_:))*