# composition(withIdentifier:)

**Framework**: Quartz  
**Kind**: method

Returns the composition that corresponds to the identifier.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func composition(withIdentifier identifier: String!) -> QCComposition!
```

#### Return Value

The composition identified by the provided string, or `nil` if there is no composition with that identifier in the composition repository.

## Parameters

- `identifier`: A string that uniquely identifies the composition to retrieve.

## See Also

- [func compositions(withProtocols: [Any]!, andAttributes: [AnyHashable : Any]!) -> [Any]!](qccompositionrepository/compositions(withprotocols:andattributes:).md)
  Returns an array of compositions that match a set of criteria.
- [func allCompositions() -> [Any]!](qccompositionrepository/allcompositions.md)
  Returns an array that contains all compositions currently in the composition repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository/composition(withidentifier:))*