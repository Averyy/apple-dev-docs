# LSMMapCompile(_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapCompile(_ mapref: LSMMap) -> OSStatus
```

```c
OSStatus LSMMapCompile(LSMMapRef mapref);
```

## Discussion

This function is computationally expensive.

## See Also

### Starting Classification Mode
- [func LSMMapCreateClusters(CFAllocator?, LSMMap, CFArray?, CFIndex, CFOptionFlags) -> Unmanaged<CFArray>?](./lsmmapcreateclusters%28_,_,_,_,_%29.md)
  Computes a set of clusters that group similar categories or words.
- [Clustering Flags](./clustering-flags.md)
  Options for creating clusters.
- [func LSMMapApplyClusters(LSMMap, CFArray) -> OSStatus](./lsmmapapplyclusters%28_,_%29.md)
  Groups categories or words (tokens) into the specified sets of clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapcompile(_:))*