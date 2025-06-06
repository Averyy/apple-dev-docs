# LSMResultGetScore(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Returns the likelihood of the specified result.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMResultGetScore(_ result: LSMResult, _ n: CFIndex) -> Float
```

#### Discussion

A [`nan`](https://developer.apple.com/documentation/kernel/1557310-nan) score typically indicates that the category doesn’t contain any token.

## See Also

- [func LSMResultGetCount(LSMResult) -> CFIndex](lsmresultgetcount(_:).md)
  Returns the number of results.
- [func LSMResultGetCategory(LSMResult, CFIndex) -> LSMCategory](lsmresultgetcategory(_:_:).md)
  Returns the category of the specified result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultgetscore(_:_:))*