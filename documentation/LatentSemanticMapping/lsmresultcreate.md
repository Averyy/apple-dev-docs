# LSMResultCreate(_:_:_:_:_:)

**Framework**: Latent Semantic Mapping  
**Kind**: func

Returns the categories or words that best match when a text is mapped into a map, in decreasing order of likelihood.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func LSMResultCreate(_ alloc: CFAllocator?, _ mapref: LSMMap, _ textref: LSMText, _ numResults: CFIndex, _ flags: CFOptionFlags) -> Unmanaged<LSMResult>
```

## See Also

- [Result Flags](result-flags.md)
  Options for creating a result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/lsmresultcreate(_:_:_:_:_:))*