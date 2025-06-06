# LSMMapCompile(_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMMapCompile(_ mapref: LSMMap) -> OSStatus
```

#### Discussion

This function is computationally expensive.

## See Also

- [func LSMMapCreateClusters(CFAllocator?, LSMMap, CFArray?, CFIndex, CFOptionFlags) -> Unmanaged<CFArray>?](lsmmapcreateclusters(_:_:_:_:_:).md)
  Computes a set of clusters that group similar categories or words.
- [Clustering Flags](clustering-flags.md)
  Options for creating clusters.
- [func LSMMapApplyClusters(LSMMap, CFArray) -> OSStatus](lsmmapapplyclusters(_:_:).md)
  Groups categories or words (tokens) into the specified sets of clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapcompile(_:))*