# allCompositions()

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns an array that contains all compositions currently in the composition repository.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func allCompositions() -> [Any]!
```

```objc
- (NSArray *) allCompositions;
```

## Return Value

An array of [`QCComposition`](../qccomposition.md) objects.

## See Also

### Fetching Compositions
- [func composition(withIdentifier: String!) -> QCComposition!](./composition%28withidentifier%29.md)
  Returns the composition that corresponds to the identifier.
- [func compositions(withProtocols: [Any]!, andAttributes: [AnyHashable : Any]!) -> [Any]!](./compositions%28withprotocols,andattributes%29.md)
  Returns an array of compositions that match a set of criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository/allcompositions())*