# LSMMapApplyClusters(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Groups categories or words (tokens) into the specified sets of clusters.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMMapApplyClusters(_ mapref: LSMMap, _ clusters: CFArray) -> OSStatus
```

```c
OSStatus LSMMapApplyClusters(LSMMapRef mapref, CFArrayRef clusters);
```

## See Also

### Starting Classification Mode
- [func LSMMapCompile(LSMMap) -> OSStatus](./lsmmapcompile%28_%29.md)
  Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.
- [func LSMMapCreateClusters(CFAllocator?, LSMMap, CFArray?, CFIndex, CFOptionFlags) -> Unmanaged<CFArray>?](./lsmmapcreateclusters%28_,_,_,_,_%29.md)
  Computes a set of clusters that group similar categories or words.
- [Clustering Flags](./clustering-flags.md)
  Options for creating clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmmapapplyclusters(_:_:))*