# LSMResult

**Framework**: Latent Semantic Mapping  
**Kind**: class  
**Role**: Class

A result of a lookup in a map.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
class LSMResult
```

```c
typedef struct __LSMResult * LSMResultRef;
```

## Overview

An [`LSMResult`](./lsmresult.md) is an immutable, opaque Core Foundation type that represents the result of a lookup.

## Topics

### Creating a Result
- [func LSMResultCreate(CFAllocator?, LSMMap, LSMText, CFIndex, CFOptionFlags) -> Unmanaged<LSMResult>](./lsmresultcreate%28_,_,_,_,_%29.md)
  Returns the categories or words that best match when a text is mapped into a map, in decreasing order of likelihood.
- [Result Flags](./result-flags.md)
  Options for creating a result.
### Querying Result Information
- [func LSMResultGetCount(LSMResult) -> CFIndex](./lsmresultgetcount%28_%29.md)
  Returns the number of results.
- [func LSMResultGetCategory(LSMResult, CFIndex) -> LSMCategory](./lsmresultgetcategory%28_,_%29.md)
  Returns the category of the specified result.
- [func LSMResultGetScore(LSMResult, CFIndex) -> Float](./lsmresultgetscore%28_,_%29.md)
  Returns the likelihood of the specified result.
### Getting a Result
- [func LSMResultCopyToken(LSMResult, CFIndex) -> Unmanaged<CFData>?](./lsmresultcopytoken%28_,_%29.md)
  Returns the token for the n-th best (zero-based) result.
- [func LSMResultCopyTokenCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](./lsmresultcopytokencluster%28_,_%29.md)
  Returns the cluster of tokens for the n-th best (zero-based) result.
- [func LSMResultCopyWord(LSMResult, CFIndex) -> Unmanaged<CFString>?](./lsmresultcopyword%28_,_%29.md)
  Returns the word for the n-th best (zero-based) result.
- [func LSMResultCopyWordCluster(LSMResult, CFIndex) -> Unmanaged<CFArray>?](./lsmresultcopywordcluster%28_,_%29.md)
  Returns the cluster of words for the n-th best (zero-based) result.
### Getting the Type Identifier
- [func LSMResultGetTypeID() -> CFTypeID](./lsmresultgettypeid%28%29.md)
  Returns the Core Foundation type identifier for Latent Semantic Mapping results.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Text Classification
- [class LSMMap](./lsmmap.md)
  A map between a set of categories and related text.
- [class LSMText](./lsmtext.md)
  An input text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresult)*