# LSMResultGetScore(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Returns the likelihood of the specified result.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMResultGetScore(_ result: LSMResult, _ n: CFIndex) -> Float
```

```c
float LSMResultGetScore(LSMResultRef result, CFIndex n);
```

#### Discussion

A [`nan`](../kernel/api-1557310-nan.md) score typically indicates that the category doesn’t contain any token.

## See Also

### Querying Result Information
- [func LSMResultGetCount(LSMResult) -> CFIndex](./lsmresultgetcount%28_%29.md)
  Returns the number of results.
- [func LSMResultGetCategory(LSMResult, CFIndex) -> LSMCategory](./lsmresultgetcategory%28_,_%29.md)
  Returns the category of the specified result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultgetscore(_:_:))*