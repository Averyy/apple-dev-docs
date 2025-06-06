# LSMResultCopyWord(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Returns the word for the n-th best (zero-based) result.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMResultCopyWord(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFString>?
```

## See Also

- [func LSMResultCopyToken(LSMResult, CFIndex) -> Unmanaged<CFData>?](lsmresultcopytoken(_:_:).md)
  Returns the token for the n-th best (zero-based) result.
- [func LSMResultCopyTokenCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopytokencluster(_:_:).md)
  Returns the cluster of tokens for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopywordcluster(_:_:).md)
  Returns the cluster of words for the n-th best (zero-based) result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultcopyword(_:_:))*