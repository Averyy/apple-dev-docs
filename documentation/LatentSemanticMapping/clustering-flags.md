# Clustering Flags

**Framework**: Latent Semantic Mapping  
**Role**: API Collection

Options for creating clusters.

#### Overview

Specify these options for [`LSMMapCreateClusters(_:_:_:_:_:)`](./lsmmapcreateclusters%28_,_,_,_,_%29.md).

## Topics

### Constants
- [var kLSMClusterCategories: Int](./klsmclustercategories.md)
  An option that specifies to cluster categories.
- [var kLSMClusterWords: Int](./klsmclusterwords.md)
  An option that specifies to cluster words.
- [var kLSMClusterTokens: Int](./klsmclustertokens.md)
  An option that specifies to cluster binary tokens.
- [var kLSMClusterKMeans: Int](./klsmclusterkmeans.md)
  An option that specifies to cluster using a k-means algorithm.
- [var kLSMClusterAgglomerative: Int](./klsmclusteragglomerative.md)
  An option that specifies to cluster using an agglomerative algorithm.

## See Also

### Starting Classification Mode
- [func LSMMapCompile(LSMMap) -> OSStatus](./lsmmapcompile%28_%29.md)
  Compiles the map into executable form and puts it into mapping mode, preparing it for the classification of texts.
- [func LSMMapCreateClusters(CFAllocator?, LSMMap, CFArray?, CFIndex, CFOptionFlags) -> Unmanaged<CFArray>?](./lsmmapcreateclusters%28_,_,_,_,_%29.md)
  Computes a set of clusters that group similar categories or words.
- [func LSMMapApplyClusters(LSMMap, CFArray) -> OSStatus](./lsmmapapplyclusters%28_,_%29.md)
  Groups categories or words (tokens) into the specified sets of clusters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/clustering-flags)*