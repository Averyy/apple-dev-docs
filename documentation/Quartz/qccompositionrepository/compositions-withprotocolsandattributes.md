# compositions(withProtocols:andAttributes:)

**Framework**: Quartz  
**Kind**: method

Returns an array of compositions that match a set of criteria.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func compositions(withProtocols protocols: [Any]!, andAttributes attributes: [AnyHashable : Any]! = [:]) -> [Any]!
```

#### Return Value

An array of [`QCComposition`](qccomposition.md) objects that meet the supplied criteria.

## Parameters

- `protocols`: The protocols that you want compositions to conform to. Pass   if you don’t want to filter based on the protocol. You can pass any of these protocols: QCCompositionProtocolAnimation, QCCompositionProtocolImageProducer, QCCompositionProtocolImageFilter, QCCompositionProtocolImageCompositor, and QCCompositionProtocolScreenSaverRSS.
- `attributes`: A dictionary that contains the attributes, and their associated values, that you want compositions  to match. Pass   if you don’t want to filter based on the attributes. For example, you can pass any of these attributes: QCCompositionAttributeNameKey, QCCompositionAttributeDescriptionKey, QCCompositionAttributeCopyrightKey, and QCCompositionAttributeBuiltInKey.

## See Also

- [func composition(withIdentifier: String!) -> QCComposition!](qccompositionrepository/composition(withidentifier:).md)
  Returns the composition that corresponds to the identifier.
- [func allCompositions() -> [Any]!](qccompositionrepository/allcompositions.md)
  Returns an array that contains all compositions currently in the composition repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository/compositions(withprotocols:andattributes:))*