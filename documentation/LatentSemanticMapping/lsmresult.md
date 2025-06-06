# LSMResult

**Framework**: Latent Semantic Mapping  
**Kind**: class

A result of a lookup in a map.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
class LSMResult
```

#### Overview

An [`LSMResult`](lsmresult.md) is an immutable, opaque Core Foundation type that represents the result of a lookup.

## Topics

### Creating a Result
- [func LSMResultCreate(CFAllocator?, LSMMap, LSMText, CFIndex, CFOptionFlags) -> Unmanaged<LSMResult>](lsmresultcreate(_:_:_:_:_:).md)
  Returns the categories or words that best match when a text is mapped into a map, in decreasing order of likelihood.
- [Result Flags](result-flags.md)
  Options for creating a result.
### Querying Result Information
- [func LSMResultGetCount(LSMResult) -> CFIndex](lsmresultgetcount(_:).md)
  Returns the number of results.
- [func LSMResultGetCategory(LSMResult, CFIndex) -> LSMCategory](lsmresultgetcategory(_:_:).md)
  Returns the category of the specified result.
- [func LSMResultGetScore(LSMResult, CFIndex) -> Float](lsmresultgetscore(_:_:).md)
  Returns the likelihood of the specified result.
### Getting a Result
- [func LSMResultCopyToken(LSMResult, CFIndex) -> Unmanaged<CFData>?](lsmresultcopytoken(_:_:).md)
  Returns the token for the n-th best (zero-based) result.
- [func LSMResultCopyTokenCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopytokencluster(_:_:).md)
  Returns the cluster of tokens for the n-th best (zero-based) result.
- [func LSMResultCopyWord(LSMResult, CFIndex) -> Unmanaged<CFString>?](lsmresultcopyword(_:_:).md)
  Returns the word for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](lsmresultcopywordcluster(_:_:).md)
  Returns the cluster of words for the n-th best (zero-based) result.
### Getting the Type Identifier
- [func LSMResultGetTypeID() -> CFTypeID](lsmresultgettypeid().md)
  Returns the Core Foundation type identifier for Latent Semantic Mapping results.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class LSMMap](lsmmap.md)
  A map between a set of categories and related text.
- [class LSMText](lsmtext.md)
  An input text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresult)*