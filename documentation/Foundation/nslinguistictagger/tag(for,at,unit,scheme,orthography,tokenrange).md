# tag(for:at:unit:scheme:orthography:tokenRange:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 4.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
class func tag(for string: String, at charIndex: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, orthography: NSOrthography?, tokenRange: NSRangePointer?) -> NSLinguisticTag?
```

```objc
+ (NSLinguisticTag) tagForString:(NSString *) string atIndex:(NSUInteger) charIndex unit:(NSLinguisticTaggerUnit) unit scheme:(NSLinguisticTagScheme) scheme orthography:(NSOrthography *) orthography tokenRange:(NSRangePointer) tokenRange;
```

## Return Value

Returns the tag for the requested tag scheme and linguistic unit, or `nil`. If a tag is returned, this function returns by reference the range of the token to `tokenRange`.

## Discussion

This is a convenience method for initializing a linguistic tagger, setting the [`string`](./string.md) property, and calling the [`tag(for:at:unit:scheme:orthography:tokenRange:)`](./tag%28for,at,unit,scheme,orthography,tokenrange%29.md) method. If you analyze the same string more than once, you should create a linguistic tagger object instead of calling this method.

## Parameters

- `string`: The position of the initial character.
- `charIndex`: The linguistic unit. See [`NSLinguisticTaggerUnit`](../nslinguistictaggerunit.md) for possible values.
- `unit`: The tag scheme. See [`NSLinguisticTagScheme`](../nslinguistictagscheme.md) for possible values.
- `scheme`: A pointer to the token range.

## See Also

### Getting Linguistic Tags
- [func tag(at: Int, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28at,unit,scheme,tokenrange%29.md)
  Returns a tag for a single scheme, for a given linguistic unit, at the specified character position.
- [func tag(at: Int, scheme: NSLinguisticTagScheme, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?) -> NSLinguisticTag?](./tag%28at,scheme,tokenrange,sentencerange%29.md)
  Returns a tag for a single scheme at the specified character position.
- [func tags(in: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./tags%28in,unit,scheme,options,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string range and linguistic unit.
- [func tags(in: NSRange, scheme: String, options: NSLinguisticTagger.Options, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]](./tags%28in,scheme,options,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string range.
- [class func tags(for: String, range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./tags%28for,range,unit,scheme,options,orthography,tokenranges%29.md)
  Returns an array of linguistic tags and token ranges for a given string and linguistic unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tag(for:at:unit:scheme:orthography:tokenrange:))*