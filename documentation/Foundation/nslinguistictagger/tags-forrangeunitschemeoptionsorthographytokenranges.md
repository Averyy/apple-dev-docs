# tags(for:range:unit:scheme:options:orthography:tokenRanges:)

**Framework**: Foundation  
**Kind**: method

Returns an array of linguistic tags and token ranges for a given string and linguistic unit.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func tags(for string: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]
```

#### Return Value

An array of the tags in the requested range.

#### Discussion

When the returned array contains an entry that doesn’t have a corresponding tag scheme, that entry is an empty string (`""`).

This is a convenience method for initializing a linguistic tagger, setting the [`string`](nslinguistictagger/string.md) property, and calling the [`tags(in:unit:scheme:options:tokenRanges:)`](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md) method. If you analyze the same string more than once, you should create a linguistic tagger object instead of calling this method.

## Parameters

- `string`: The range from which to return tags.
- `range`: The linguistic unit. See   for possible values.
- `unit`: The tag scheme. See   for possible values.
- `scheme`: The linguistic tagger options to use. See   for possible values.
- `options`: Returns by reference an array of token ranges.

## See Also

- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:unit:scheme:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [func tag(at: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:).md)
  Returns a tag for a single scheme at the specified character position.
- [class func tag(for: String, at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tags(in: NSRange, scheme: String, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]](nslinguistictagger/tags(in:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:))*