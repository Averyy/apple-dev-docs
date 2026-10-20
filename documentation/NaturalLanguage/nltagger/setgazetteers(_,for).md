# setGazetteers(_:for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Attaches gazetteers to a tag scheme, typically one gazetteer per language or one language-independent gazetteer.

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
func setGazetteers(_ gazetteers: [NLGazetteer], for tagScheme: NLTagScheme)
```

```objc
- (void) setGazetteers:(NSArray<NLGazetteer *> *) gazetteers forTagScheme:(NLTagScheme) tagScheme;
```

## Parameters

- `gazetteers`: The gazetteers to attach to a tag scheme.
- `tagScheme`: The tag scheme for the gazetteers.

## See Also

### Using gazetteers with a tagger
- [func gazetteers(for: NLTagScheme) -> [NLGazetteer]](./gazetteers%28for%29.md)
  Retrieves the gazetteers attached to a tag scheme.
- [class NLGazetteer](../nlgazetteer.md)
  A collection of terms and their labels, which take precedence over a word tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/setgazetteers(_:for:))*