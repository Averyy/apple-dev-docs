# LSMResultCopyToken(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Returns the token for the n-th best (zero-based) result.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMResultCopyToken(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFData>?
```

```c
CFDataRefLSMResultCopyToken(LSMResultRef result, CFIndex n);
```

## See Also

### Getting a Result
- [func LSMResultCopyTokenCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](./lsmresultcopytokencluster%28_,_%29.md)
  Returns the cluster of tokens for the n-th best (zero-based) result.
- [func LSMResultCopyWord(LSMResult, CFIndex) -> Unmanaged<CFString>?](./lsmresultcopyword%28_,_%29.md)
  Returns the word for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](./lsmresultcopywordcluster%28_,_%29.md)
  Returns the cluster of words for the n-th best (zero-based) result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultcopytoken(_:_:))*