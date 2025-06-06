# tag(at:scheme:tokenRange:sentenceRange:)

**Framework**: Foundation  
**Kind**: method

Returns a tag for a single scheme at the specified character position.

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
func tag(at charIndex: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?
```

#### Return Value

Returns the tag for the requested tag scheme, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`, and the range of the enclosing sentence to `sentenceRange`, if applicable.

#### Discussion

This is a convenience method for calling [`tag(at:unit:scheme:tokenRange:)`](nslinguistictagger/tag(at:unit:scheme:tokenrange:).md) and passing [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `charIndex`: The position of the initial character.
- `scheme`: The tag scheme. See   for the possible values.
- `tokenRange`: A pointer to the token range.
- `sentenceRange`: A pointer to the range of the sentence.

## See Also

- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(at:unit:scheme:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [class func tag(for: String, at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?](nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:).md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(in:unit:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tags(in: NSRange, scheme: String, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]](nslinguistictagger/tags(in:scheme:options:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string range.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nslinguistictagger/tags(for:range:unit:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:))*