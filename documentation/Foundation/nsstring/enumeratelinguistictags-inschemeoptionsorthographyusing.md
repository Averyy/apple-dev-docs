# enumerateLinguisticTags(in:scheme:options:orthography:using:)

**Framework**: Foundation  
**Kind**: method

Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.

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
func enumerateLinguisticTags(in range: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], orthography: NSOrthography?, using block: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

This is a convenience method.  It is the equivalent of creating an instance of `NSLinguisticTagger`, specifying the receiver as the string to be analyzed, and the orthography (or `nil`) and then invoking the [`NSLinguisticTagger`](nslinguistictagger.md) method or [`enumerateTags(in:scheme:options:using:)`](nslinguistictagger/enumeratetags(in:scheme:options:using:).md).

## Parameters

- `range`: The range of the string to analyze.
- `scheme`: The tag scheme to use. See Linguistic Tag Schemes for supported values.
- `options`: The linguistic tagger options to use. See  for the constants. These constants can be combined using the C-Bitwise OR operator.
- `orthography`: The orthography of the string. If  , the linguistic tagger will attempt to determine the orthography from the string content.
- `block`: The block takes four arguments:

## See Also

- [func linguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nsstring/linguistictags(in:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags for the specified range and requested tags within the receiving string.
- [NSString.EnumerationOptions](nsstring/enumerationoptions.md)
  Constants to specify kinds of substrings and styles of enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:))*