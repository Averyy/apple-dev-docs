# Map Properties

**Framework**: Latent Semantic Mapping

Special properties that determine a map’s behavior.

#### Overview

Latent Semantic Mapping interprets the following keys. All other keys starting with `LSM` are reserved.

## Topics

### Properties
- [var kLSMAlgorithmKey: String](klsmalgorithmkey.md)
  A key that specifies which algorithm to use.
- [var kLSMAlgorithmDense: String](klsmalgorithmdense.md)
  A value that specifies to perform a singular value decomposition (SVD) on a dense matrix.
- [var kLSMAlgorithmSparse: String](klsmalgorithmsparse.md)
  A value that specifies to perform a singular value decomposition (SVD) on a sparse matrix.
- [var kLSMPrecisionKey: String](klsmprecisionkey.md)
  A key that specifies the precision to use.
- [var kLSMPrecisionFloat: String](klsmprecisionfloat.md)
  A value that specifies to use float arithmetic.
- [var kLSMPrecisionDouble: String](klsmprecisiondouble.md)
  A value that specifies to use double arithmetic.
- [var kLSMDimensionKey: String](klsmdimensionkey.md)
  A key that specifies the number of singular values to compute.
- [var kLSMIterationsKey: String](klsmiterationskey.md)
  A key that specifies the number of iterations to compute.
- [var kLSMSweepAgeKey: String](klsmsweepagekey.md)
  A key that specifies the number of days between sweeping generations.
- [var kLSMSweepCutoffKey: String](klsmsweepcutoffkey.md)
  A key that specifies the minimum count to keep entry.

## See Also

- [func LSMMapSetProperties(LSMMap, CFDictionary)](lsmmapsetproperties(_:_:).md)
  Sets a dictionary of properties for the map.
- [func LSMMapGetProperties(LSMMap) -> Unmanaged<CFDictionary>](lsmmapgetproperties(_:).md)
  Gets a dictionary of properties for the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/map-properties)*