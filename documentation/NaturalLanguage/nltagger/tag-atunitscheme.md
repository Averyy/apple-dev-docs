# tag(at:unit:scheme:)

**Framework**: Natural Language  
**Kind**: method

Finds a tag for a given linguistic unit, for a single scheme, at the specified character position.

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
func tag(at index: String.Index, unit: NLTokenUnit, scheme: NLTagScheme) -> (NLTag?, Range<String.Index>)
```

#### Return Value

The tag for the requested tag scheme and linguistic unit, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`.

## Parameters

- `unit`: The linguistic unit. See   for possible values.
- `scheme`: The tag scheme. See   for possible values.

## See Also

- [func tags(in: Range<String.Index>, unit: NLTokenUnit, scheme: NLTagScheme, options: NLTagger.Options) -> [(NLTag?, Range<String.Index>)]](nltagger/tags(in:unit:scheme:options:).md)
  Finds an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tagHypotheses(at: String.Index, unit: NLTokenUnit, scheme: NLTagScheme, maximumCount: Int) -> ([String : Double], Range<String.Index>)](nltagger/taghypotheses(at:unit:scheme:maximumcount:).md)
  Finds multiple possible tags for a given linguistic unit, for a single scheme, at the specified character position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tag(at:unit:scheme:))*