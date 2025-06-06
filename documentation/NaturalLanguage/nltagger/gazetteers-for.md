# gazetteers(for:)

**Framework**: Natural Language  
**Kind**: method

Retrieves the gazetteers attached to a tag scheme.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func gazetteers(for tagScheme: NLTagScheme) -> [NLGazetteer]
```

#### Return Value

An array of [`NLGazetteer`](nlgazetteer.md).

## Parameters

- `tagScheme`: The tag scheme for the gazetteers.

## See Also

- [func setGazetteers([NLGazetteer], for: NLTagScheme)](nltagger/setgazetteers(_:for:).md)
  Attaches gazetteers to a tag scheme, typically one gazetteer per language or one language-independent gazetteer.
- [class NLGazetteer](nlgazetteer.md)
  A collection of terms and their labels, which take precedence over a word tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/gazetteers(for:))*