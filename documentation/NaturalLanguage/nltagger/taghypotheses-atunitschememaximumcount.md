# tagHypotheses(at:unit:scheme:maximumCount:)

**Framework**: Natural Language  
**Kind**: method

Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@nonobjc
func tagHypotheses(at index: String.Index, unit: NLTokenUnit, scheme: NLTagScheme, maximumCount: Int) -> ([String : Double], Range<String.Index>)
```

#### Return Value

A tuple containing a dictionary and a range.

#### Discussion

Each dictionary entry is a predicted tag with its associated probability score. These tags are the top candidates proposed as possible tags for the token. The dictionary contains up to `maximumCount` entries.

The range contains the range of the individual token for which these tags were produced.

## Parameters

- `index`: The position of the initial character.
- `unit`: The linguistic unit. See   for possible values.
- `scheme`: The tag scheme. See   for possible values. Not all tag schemes produce more than one prediction.
- `maximumCount`: The maximum number of tag predictions to return.

## See Also

- [func tags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options) -> [(NLTag?, Range<String.Index>)]](nltagger/tags(in:unit:scheme:options:).md)
  Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tag(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme) -> (NLTag?, Range<String.Index>)](nltagger/tag(at:unit:scheme:).md)
  Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/taghypotheses(at:unit:scheme:maximumcount:))*