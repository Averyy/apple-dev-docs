# tag(at:scheme:tokenRange:sentenceRange:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a tag for a single scheme at the specified character position.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.7+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
func tag(at charIndex: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?
```

```objc
- (NSLinguisticTag) tagAtIndex:(NSUInteger) charIndex scheme:(NSLinguisticTagScheme) scheme tokenRange:(NSRangePointer) tokenRange sentenceRange:(NSRangePointer) sentenceRange;
```

#### Return Value

Returns the tag for the requested tag scheme, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`, and the range of the enclosing sentence to `sentenceRange`, if applicable.

#### Discussion

This is a convenience method for calling [`tag(at:unit:scheme:tokenRange:)`](./tag%28at,unit,scheme,tokenrange%29.md) and passing [`NSLinguisticTaggerUnit.word`](../nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `charIndex`: The position of the initial character.
- `scheme`: The tag scheme. See [`NSLinguisticTagScheme`](../nslinguistictagscheme.md) for the possible values.
- `tokenRange`: A pointer to the token range.
- `sentenceRange`: A pointer to the range of the sentence.

## See Also

### Getting Linguistic Tags
- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28at,unit,scheme,tokenrange%29.md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [class func tag(for: String, at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28for,at,unit,scheme,orthography,tokenrange%29.md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./tags%28in,unit,scheme,options,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tags(in: NSRange, scheme: String, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]](./tags%28in,scheme,options,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string range.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./tags%28for,range,unit,scheme,options,orthography,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tag(at:scheme:tokenrange:sentencerange:))*