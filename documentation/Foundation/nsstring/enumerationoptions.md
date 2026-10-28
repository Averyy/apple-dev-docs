# NSString.EnumerationOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSStringEnumerationOptions : NSUInteger;
```

## Overview

These options are used with the [`enumerateSubstrings(in:options:using:)`](./enumeratesubstrings%28in,options,using%29.md) method. Pass in one `NSStringEnumerationBy...` option and combine with any of the remaining enumeration style constants using the C bitwise `OR` operator.

## Topics

### Constants
- [static var byLines: NSString.EnumerationOptions](./enumerationoptions/bylines.md)
- [static var byParagraphs: NSString.EnumerationOptions](./enumerationoptions/byparagraphs.md)
- [static var byComposedCharacterSequences: NSString.EnumerationOptions](./enumerationoptions/bycomposedcharactersequences.md)
- [static var byWords: NSString.EnumerationOptions](./enumerationoptions/bywords.md)
- [static var bySentences: NSString.EnumerationOptions](./enumerationoptions/bysentences.md)
- [static var reverse: NSString.EnumerationOptions](./enumerationoptions/reverse.md)
- [static var substringNotRequired: NSString.EnumerationOptions](./enumerationoptions/substringnotrequired.md)
- [static var localized: NSString.EnumerationOptions](./enumerationoptions/localized.md)
### Initializers
- [init(some Sequence<NSString.EnumerationOptions>)](./enumerationoptions/init%28_%29.md)
- [init(rawValue: UInt)](./enumerationoptions/init%28rawvalue%29.md)
### Instance Methods
- [func contains(String.EnumerationOptions) -> Bool](./enumerationoptions/contains%28_%29.md)
- [func formIntersection(String.EnumerationOptions)](./enumerationoptions/formintersection%28_%29.md)
- [func formSymmetricDifference(String.EnumerationOptions)](./enumerationoptions/formsymmetricdifference%28_%29.md)
- [func formUnion(String.EnumerationOptions)](./enumerationoptions/formunion%28_%29.md)
- [func insert(String.EnumerationOptions) -> (inserted: Bool, memberAfterInsert: String.EnumerationOptions)](./enumerationoptions/insert%28_%29.md)
- [func isSubset(of: String.EnumerationOptions) -> Bool](./enumerationoptions/issubset%28of%29.md)
- [func remove(String.EnumerationOptions) -> String.EnumerationOptions?](./enumerationoptions/remove%28_%29.md)
### Type Properties
- [static var byCaretPositions: NSString.EnumerationOptions](./enumerationoptions/bycaretpositions.md)
- [static var byDeletionClusters: NSString.EnumerationOptions](./enumerationoptions/bydeletionclusters.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Performing Linguistic Analysis
- [func enumerateLinguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratelinguistictags%28in,scheme,options,orthography,using%29.md)
  Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [func linguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](./linguistictags%28in,scheme,options,orthography,tokenranges%29.md)
  Returns an array of linguistic tags for the specified range and requested tags within the receiving string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumerationoptions)*