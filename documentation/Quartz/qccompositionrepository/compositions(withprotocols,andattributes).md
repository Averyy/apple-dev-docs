# compositions(withProtocols:andAttributes:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns an array of compositions that match a set of criteria.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func compositions(withProtocols protocols: [Any]!, andAttributes attributes: [AnyHashable : Any]! = [:]) -> [Any]!
```

```objc
- (NSArray *) compositionsWithProtocols:(NSArray *) protocols andAttributes:(NSDictionary *) attributes;
```

#### Return Value

An array of [`QCComposition`](../qccomposition.md) objects that meet the supplied criteria.

## Parameters

- `protocols`: The protocols that you want compositions to conform to. Pass `nil` if you don’t want to filter based on the protocol. You can pass any of these protocols: QCCompositionProtocolAnimation, QCCompositionProtocolImageProducer, QCCompositionProtocolImageFilter, QCCompositionProtocolImageCompositor, and QCCompositionProtocolScreenSaverRSS.
- `attributes`: A dictionary that contains the attributes, and their associated values, that you want compositions  to match. Pass `nil` if you don’t want to filter based on the attributes. For example, you can pass any of these attributes: QCCompositionAttributeNameKey, QCCompositionAttributeDescriptionKey, QCCompositionAttributeCopyrightKey, and QCCompositionAttributeBuiltInKey.

## See Also

### Fetching Compositions
- [func composition(withIdentifier: String!) -> QCComposition!](./composition%28withidentifier%29.md)
  Returns the composition that corresponds to the identifier.
- [func allCompositions() -> [Any]!](./allcompositions%28%29.md)
  Returns an array that contains all compositions currently in the composition repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository/compositions(withprotocols:andattributes:))*