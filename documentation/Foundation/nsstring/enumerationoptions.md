# NSString.EnumerationOptions

**Framework**: Foundation  
**Kind**: struct

Constants to specify kinds of substrings and styles of enumeration.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct EnumerationOptions
```

#### Overview

These options are used with the [`enumerateSubstrings(in:options:using:)`](nsstring/enumeratesubstrings(in:options:using:).md) method. Pass in one `NSStringEnumerationBy...` option and combine with any of the remaining enumeration style constants using the C bitwise `OR` operator.

## Topics

### Constants
- [static var byLines: NSString.EnumerationOptions](nsstring/enumerationoptions/bylines.md)
- [static var byParagraphs: NSString.EnumerationOptions](nsstring/enumerationoptions/byparagraphs.md)
- [static var byComposedCharacterSequences: NSString.EnumerationOptions](nsstring/enumerationoptions/bycomposedcharactersequences.md)
- [static var byWords: NSString.EnumerationOptions](nsstring/enumerationoptions/bywords.md)
- [static var bySentences: NSString.EnumerationOptions](nsstring/enumerationoptions/bysentences.md)
- [static var reverse: NSString.EnumerationOptions](nsstring/enumerationoptions/reverse.md)
- [static var substringNotRequired: NSString.EnumerationOptions](nsstring/enumerationoptions/substringnotrequired.md)
- [static var localized: NSString.EnumerationOptions](nsstring/enumerationoptions/localized.md)
### Initializers
- [init(rawValue: UInt)](nsstring/enumerationoptions/init(rawvalue:).md)
### Type Properties
- [static var byCaretPositions: NSString.EnumerationOptions](nsstring/enumerationoptions/bycaretpositions.md)
- [static var byDeletionClusters: NSString.EnumerationOptions](nsstring/enumerationoptions/bydeletionclusters.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func enumerateLinguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:).md)
  Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [func linguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nsstring/linguistictags(in:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags for the specified range and requested tags within the receiving string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions)*