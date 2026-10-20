# LSMResultCopyTokenCluster(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Returns the cluster of tokens for the n-th best (zero-based) result.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMResultCopyTokenCluster(_ result: LSMResult, _ n: CFIndex) -> Unmanaged<CFArray>?
```

```c
CFArrayRefLSMResultCopyTokenCluster(LSMResultRef result, CFIndex n);
```

## See Also

### Getting a Result
- [func LSMResultCopyToken(LSMResult, CFIndex) -> Unmanaged<CFData>?](./lsmresultcopytoken%28_,_%29.md)
  Returns the token for the n-th best (zero-based) result.
- [func LSMResultCopyWord(LSMResult, CFIndex) -> Unmanaged<CFString>?](./lsmresultcopyword%28_,_%29.md)
  Returns the word for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](./lsmresultcopywordcluster%28_,_%29.md)
  Returns the cluster of words for the n-th best (zero-based) result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultcopytokencluster(_:_:))*