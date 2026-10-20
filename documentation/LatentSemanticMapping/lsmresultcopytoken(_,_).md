# LSMResultCopyToken(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Returns the token for the n-th best (zero-based) result.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMResultCopyToken(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFData>?
```

## See Also

- [func LSMResultCopyTokenCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopytokencluster(_:_:).md)
  Returns the cluster of tokens for the n-th best (zero-based) result.
- [func LSMResultCopyWord(LSMResult, CFIndex) -> Unmanaged<CFString>?](lsmresultcopyword(_:_:).md)
  Returns the word for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopywordcluster(_:_:).md)
  Returns the cluster of words for the n-th best (zero-based) result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultcopytoken(_:_:))*