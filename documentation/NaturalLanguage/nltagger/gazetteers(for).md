# gazetteers(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<NLGazetteer *> *) gazetteersForTagScheme:(NLTagScheme) tagScheme;
```

#### Return Value

An array of [`NLGazetteer`](../nlgazetteer.md).

## Parameters

- `tagScheme`: The tag scheme for the gazetteers.

## See Also

### Using gazetteers with a tagger
- [func setGazetteers([NLGazetteer], for: NLTagScheme)](./setgazetteers%28_,for%29.md)
  Attaches gazetteers to a tag scheme, typically one gazetteer per language or one language-independent gazetteer.
- [class NLGazetteer](../nlgazetteer.md)
  A collection of terms and their labels, which take precedence over a word tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/gazetteers(for:))*