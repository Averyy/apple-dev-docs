# tags(in:unit:scheme:options:)

**Framework**: Natural Language  
**Kind**: method

Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
func tags(in range: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options = []) -> [(NLTag?, Range<String.Index>)]
```

#### Return Value

An array of the tags in the requested range.

#### Discussion

When the returned array contains an entry that doesn’t have a corresponding tag scheme, that entry is an empty string (””).

## Parameters

- `range`: The range from which to return tags.
- `unit`: The linguistic unit. See   for possible values.
- `scheme`: The tag scheme. See   for possible values.
- `options`: The linguistic tagger options to use. See   for possible values.

## See Also

- [func tag(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme) -> (NLTag?, Range<String.Index>)](nltagger/tag(at:unit:scheme:).md)
  Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.
- [func tagHypotheses(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme, maximumCount: Int) -> ([String : Double], Range<String.Index>)](nltagger/taghypotheses(at:unit:scheme:maximumcount:).md)
  Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tags(in:unit:scheme:options:))*