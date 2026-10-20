# composition(withIdentifier:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the composition that corresponds to the identifier.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func composition(withIdentifier identifier: String!) -> QCComposition!
```

```objc
- (QCComposition *) compositionWithIdentifier:(NSString *) identifier;
```

#### Return Value

The composition identified by the provided string, or `nil` if there is no composition with that identifier in the composition repository.

## Parameters

- `identifier`: A string that uniquely identifies the composition to retrieve.

## See Also

### Fetching Compositions
- [func compositions(withProtocols: [Any]!, andAttributes: [AnyHashable : Any]!) -> [Any]!](./compositions%28withprotocols,andattributes%29.md)
  Returns an array of compositions that match a set of criteria.
- [func allCompositions() -> [Any]!](./allcompositions%28%29.md)
  Returns an array that contains all compositions currently in the composition repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository/composition(withidentifier:))*