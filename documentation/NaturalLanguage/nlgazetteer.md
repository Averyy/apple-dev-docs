# NLGazetteer

**Framework**: Natural Language  
**Kind**: class

A collection of terms and their labels, which take precedence over a word tagger.

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
class NLGazetteer
```

#### Overview

Use an [`NLGazetteer`](nlgazetteer.md) to augment an [`NLTagger`](nltagger.md) when you need to tag a specific set of terms (single words or short phrases) with a label. Typically, you add one gazetteer per language, or one language-independent gazetteer, to an [`NLTagger`](nltagger.md) with its [`setGazetteers(_:for:)`](nltagger/setgazetteers(_:for:).md) method. The tagger uses its gazetteers to look up each term it processes. If a gazetteer has a label for a term, the tagger uses that label to tag the term, instead of inferring a tag itself.

Typically, you create a gazetteer at development time, such as in a macOS playground, with Create ML’s [`MLGazetteer`](https://developer.apple.com/documentation/CreateML/MLGazetteer). Alternatively, you can create an [`NLGazetteer`](nlgazetteer.md) at runtime by using [`init(dictionary:language:)`](nlgazetteer/init(dictionary:language:).md).

## Topics

### Creating a Gazetteer
- [init(contentsOf: URL) throws](nlgazetteer/init(contentsof:).md)
  Creates a Natural Language gazetteer from a model created with the Create ML framework.
- [init(data: Data) throws](nlgazetteer/init(data:).md)
  Creates a gazetteer from a data instance.
- [init(dictionary: [String : [String]], language: NLLanguage?) throws](nlgazetteer/init(dictionary:language:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary.
- [class func write([String : [String]], language: NLLanguage?, to: URL) throws](nlgazetteer/write(_:language:to:).md)
  Creates a gazetteer from a set of labels for terms represented by a dictionary and saves the gazetteer to a file.
### Looking Up Labels for Terms
- [func label(for: String) -> String?](nlgazetteer/label(for:).md)
  Retrieves the label for the given term.
### Inspecting a Gazetteer
- [var data: Data](nlgazetteer/data.md)
  The gazetteer represented as a data instance.
- [var language: NLLanguage?](nlgazetteer/language.md)
  The language of the gazetteer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setGazetteers([NLGazetteer], for: NLTagScheme)](nltagger/setgazetteers(_:for:).md)
  Attaches gazetteers to a tag scheme, typically one gazetteer per language or one language-independent gazetteer.
- [func gazetteers(for: NLTagScheme) -> [NLGazetteer]](nltagger/gazetteers(for:).md)
  Retrieves the gazetteers attached to a tag scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlgazetteer)*