# tags(in:scheme:options:tokenRanges:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of linguistic tags and token ranges for a given string range.

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
func tags(in range: NSRange, scheme tagScheme: String, options opts: NSLinguisticTagger.Options = [], tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]
```

```objc
- (NSArray<NSString *> *) tagsInRange:(NSRange) range scheme:(NSString *) tagScheme options:(NSLinguisticTaggerOptions) opts tokenRanges:(NSArray<NSValue *> **) tokenRanges;
```

## Return Value

An array of the tags in the requested range.

## Discussion

When the returned array contains an entry that doesn’t have a corresponding tag scheme, that entry is an empty string (`""`).

This is a convenience method for calling [`tags(in:unit:scheme:options:tokenRanges:)`](./tags%28in,unit,scheme,options,tokenranges%29.md) and passing [`NSLinguisticTaggerUnit.word`](../nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `range`: The range from which to return tags.
- `tagScheme`: The tag scheme. See [`NSLinguisticTagScheme`](../nslinguistictagscheme.md) for possible values.
- `opts`: The linguistic tagger options to use. See [`NSLinguisticTagger.Options`](./options.md) for possible values.
- `tokenRanges`: Returns by reference an array of token ranges.

## See Also

### Getting Linguistic Tags
- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28at,unit,scheme,tokenrange%29.md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [func tag(at: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28at,scheme,tokenrange,sentencerange%29.md)
  Returns a tag for a single scheme at the specified character position.
- [class func tag(for: String, at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28for,at,unit,scheme,orthography,tokenrange%29.md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./tags%28in,unit,scheme,options,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./tags%28for,range,unit,scheme,options,orthography,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tags(in:scheme:options:tokenranges:))*