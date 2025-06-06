# tags(in:scheme:options:tokenRanges:)

**Framework**: Foundation  
**Kind**: method

Returns an array of linguistic tags and token ranges for a given string range.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func tags(in range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTagger.Options = [], tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]
```

#### Return Value

An array of the tags in the requested range.

#### Discussion

When the returned array contains an entry that doesn’t have a corresponding tag scheme, that entry is an empty string (`""`).

This is a convenience method for calling [`tags(in:unit:scheme:options:tokenRanges:)`](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md) and passing [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `range`: The range from which to return tags.
- `tagScheme`: The tag scheme. See   for possible values.
- `opts`: The linguistic tagger options to use. See   for possible values.
- `tokenRanges`: Returns by reference an array of token ranges.

## See Also

- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:unit:scheme:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [func tag(at: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:).md)
  Returns a tag for a single scheme at the specified character position.
- [class func tag(for: String, at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tags(in:scheme:options:tokenranges:))*