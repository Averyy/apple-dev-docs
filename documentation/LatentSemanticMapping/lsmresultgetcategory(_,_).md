# LSMResultGetCategory(_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func  
**Role**: Function

Returns the category of the specified result.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func LSMResultGetCategory(_ result: LSMResult, _ n: CFIndex) -> LSMCategory
```

```c
LSMCategory LSMResultGetCategory(LSMResultRef result, CFIndex n);
```

## See Also

### Querying Result Information
- [func LSMResultGetCount(LSMResult) -> CFIndex](./lsmresultgetcount%28_%29.md)
  Returns the number of results.
- [func LSMResultGetScore(LSMResult, CFIndex) -> Float](./lsmresultgetscore%28_,_%29.md)
  Returns the likelihood of the specified result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultgetcategory(_:_:))*