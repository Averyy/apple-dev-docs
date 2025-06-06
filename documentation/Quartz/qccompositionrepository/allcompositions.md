# allCompositions()

**Framework**: Quartz  
**Kind**: method

Returns an array that contains all compositions currently in the composition repository.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func allCompositions() -> [Any]!
```

#### Return Value

An array of [`QCComposition`](qccomposition.md) objects.

## See Also

- [func composition(withIdentifier: String!) -> QCComposition!](qccompositionrepository/composition(withidentifier:).md)
  Returns the composition that corresponds to the identifier.
- [func compositions(withProtocols: [Any]!, andAttributes: [AnyHashable : Any]!) -> [Any]!](qccompositionrepository/compositions(withprotocols:andattributes:).md)
  Returns an array of compositions that match a set of criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository/allcompositions())*