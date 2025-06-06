# LSMResultCopyTokenCluster(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Returns the cluster of tokens for the n-th best (zero-based) result.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMResultCopyTokenCluster(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFArray>?
```

## See Also

- [func LSMResultCopyToken(LSMResult, CFIndex) -> Unmanaged<CFData>?](lsmresultcopytoken(_:_:).md)
  Returns the token for the n-th best (zero-based) result.
- [func LSMResultCopyWord(LSMResult, CFIndex) -> Unmanaged<CFString>?](lsmresultcopyword(_:_:).md)
  Returns the word for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopywordcluster(_:_:).md)
  Returns the cluster of words for the n-th best (zero-based) result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultcopytokencluster(_:_:))*