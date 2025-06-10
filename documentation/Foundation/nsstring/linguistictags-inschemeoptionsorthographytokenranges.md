# linguisticTags(in:scheme:options:orthography:tokenRanges:)

**Framework**: Foundation  
**Kind**: method

Returns an array of linguistic tags for the specified range and requested tags within the receiving string.

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
func linguisticTags(in range: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]
```

#### Return Value

Returns an array containing the linguistic tags for the `tokenRanges` within the receiving string.

#### Discussion

This is a convenience method.  It is the equivalent of creating an instance of [`NSLinguisticTagger`](nslinguistictagger.md), specifying the receiver as the string to be analyzed, and the orthography (or `nil`) and then invoking the [`NSLinguisticTagger`](nslinguistictagger.md) method or [`linguisticTags(in:scheme:options:orthography:tokenRanges:)`](nsstring/linguistictags(in:scheme:options:orthography:tokenranges:).md).

## Parameters

- `range`: The range of the string to analyze.
- `scheme`: The tag scheme to use. See Linguistic Tag Schemes for supported values.
- `options`: The linguistic tagger options to use. See   for the constants. These constants can be combined using the C-Bitwise OR operator.
- `orthography`: The orthography of the string. If  , the linguistic tagger will attempt to determine the orthography from the string content.
- `tokenRanges`: An array returned by-reference containing the token ranges of the linguistic tags wrapped in   objects.

## See Also

- [func enumerateLinguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:).md)
  Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [NSString.EnumerationOptions](nsstring/enumerationoptions.md)
  Constants to specify kinds of substrings and styles of enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/linguistictags(in:scheme:options:orthography:tokenranges:))*