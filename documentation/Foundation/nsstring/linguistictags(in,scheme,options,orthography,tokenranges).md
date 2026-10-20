# linguisticTags(in:scheme:options:orthography:tokenRanges:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of linguistic tags for the specified range and requested tags within the receiving string.

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
func linguisticTags(in range: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]
```

```objc
- (NSArray<NSString *> *) linguisticTagsInRange:(NSRange) range scheme:(NSLinguisticTagScheme) scheme options:(NSLinguisticTaggerOptions) options orthography:(NSOrthography *) orthography tokenRanges:(NSArray<NSValue *> **) tokenRanges;
```

#### Return Value

Returns an array containing the linguistic tags for the `tokenRanges` within the receiving string.

#### Discussion

This is a convenience method.  It is the equivalent of creating an instance of [`NSLinguisticTagger`](../nslinguistictagger.md), specifying the receiver as the string to be analyzed, and the orthography (or `nil`) and then invoking the [`NSLinguisticTagger`](../nslinguistictagger.md) method or [`linguisticTags(in:scheme:options:orthography:tokenRanges:)`](./linguistictags%28in,scheme,options,orthography,tokenranges%29.md).

## Parameters

- `range`: The range of the string to analyze.
- `scheme`: The tag scheme to use. See Linguistic Tag Schemes for supported values.
- `options`: The linguistic tagger options to use. See [`NSLinguisticTagger.Options`](../nslinguistictagger/options.md) for the constants. These constants can be combined using the C-Bitwise OR operator.
- `orthography`: The orthography of the string. If `nil`, the linguistic tagger will attempt to determine the orthography from the string content.
- `tokenRanges`: An array returned by-reference containing the token ranges of the linguistic tags wrapped in `NSValue` objects.

## See Also

### Performing Linguistic Analysis
- [func enumerateLinguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratelinguistictags%28in,scheme,options,orthography,using%29.md)
  Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [NSString.EnumerationOptions](./enumerationoptions.md)
  Constants to specify kinds of substrings and styles of enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/linguistictags(in:scheme:options:orthography:tokenranges:))*