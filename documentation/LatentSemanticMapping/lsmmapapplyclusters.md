# LSMMapApplyClusters(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Groups categories or words (tokens) into the specified sets of clusters.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapApplyClusters(_ mapref: LSMMap, _ clusters: CFArray) -> OSStatus
```

## See Also

- [func LSMMapCompile(LSMMap) -> OSStatus](lsmmapcompile(_:).md)
  Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.
- [func LSMMapCreateClusters(CFAllocator?, LSMMap, CFArray?, CFIndex, CFOptionFlags) -> Unmanaged<CFArray>?](lsmmapcreateclusters(_:_:_:_:_:).md)
  Computes a set of clusters that group similar categories or words.
- [Clustering Flags](clustering-flags.md)
  Options for creating clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapapplyclusters(_:_:))*