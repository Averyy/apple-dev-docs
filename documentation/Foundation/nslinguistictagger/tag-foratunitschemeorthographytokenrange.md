# tag(for:at:unit:scheme:orthography:tokenRange:)

**Framework**: Foundation  
**Kind**: method

Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.

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
class func tag(for string: String, at charIndex: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?
```

#### Return Value

Returns the tag for the requested tag scheme and linguistic unit, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`.

#### Discussion

This is a convenience method for initializing a linguistic tagger, setting the [`string`](nslinguistictagger/string.md) property, and calling the [`tag(for:at:unit:scheme:orthography:tokenRange:)`](nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:).md) method. If you analyze the same string more than once, you should create a linguistic tagger object instead of calling this method.

## Parameters

- `string`: The position of the initial character.
- `charIndex`: The linguistic unit. See   for possible values.
- `unit`: The tag scheme. See   for possible values.
- `scheme`: A pointer to the token range.

## See Also

- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:unit:scheme:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [func tag(at: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:).md)
  Returns a tag for a single scheme at the specified character position.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tags(in: NSRange, scheme: String, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]](nslinguistictagger/tags(in:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:))*