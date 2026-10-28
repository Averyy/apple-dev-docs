# enumerateLinguisticTags(in:scheme:options:orthography:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.

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
func enumerateLinguisticTags(in range: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, using block: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateLinguisticTagsInRange:(NSRange) range scheme:(NSLinguisticTagScheme) scheme options:(NSLinguisticTaggerOptions) options orthography:(NSOrthography *) orthography usingBlock:(void (^)(NSLinguisticTag tag, NSRange tokenRange, NSRange sentenceRange, BOOL *stop)) block;
```

## Discussion

This is a convenience method.  It is the equivalent of creating an instance of `NSLinguisticTagger`, specifying the receiver as the string to be analyzed, and the orthography (or `nil`) and then invoking the [`NSLinguisticTagger`](../nslinguistictagger.md) method or [`enumerateTags(in:scheme:options:using:)`](../nslinguistictagger/enumeratetags%28in,scheme,options,using%29.md).

## Parameters

- `range`: The range of the string to analyze.
- `scheme`: The tag scheme to use. See Linguistic Tag Schemes for supported values.
- `options`: The linguistic tagger options to use. See [`NSLinguisticTagger.Options`](../nslinguistictagger/options.md)for the constants. These constants can be combined using the C-Bitwise OR operator.
- `orthography`: The orthography of the string. If `nil`, the linguistic tagger will attempt to determine the orthography from the string content.
- `block`: The Block to apply to the string.

  The block takes four arguments:

  - **tag**: The tag scheme for the token. The opts parameter specifies the types of tagger options that are located.
  - **tokenRange**: The range of a string matching the tag scheme.
  - **sentenceRange**: The range of the sentence in which the token is found.
  - **stop**: A reference to a Boolean value. The block can set the value to [`true`](../../Swift/true.md) to stop further processing of the array. The `stop` argument is an out-only argument. You should only ever set this Boolean to [`true`](../../Swift/true.md) within the Block.

## See Also

### Performing Linguistic Analysis
- [func linguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./linguistictags%28in,scheme,options,orthography,tokenranges%29.md)
  Returns an array of linguistic tags for the specified range and requested tags within the receiving string.
- [NSString.EnumerationOptions](./enumerationoptions.md)
  Constants to specify kinds of substrings and styles of enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:))*