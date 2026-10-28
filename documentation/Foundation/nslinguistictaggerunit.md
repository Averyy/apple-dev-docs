# NSLinguisticTaggerUnit

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants representing linguistic units.

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
enum NSLinguisticTaggerUnit
```

```c
enum NSLinguisticTaggerUnit : NSInteger;
```

## Overview

You use these constants with the [`availableTagSchemes(for:language:)`](./nslinguistictagger/availabletagschemes%28for,language%29.md) method as well as the [`tag(for:at:unit:scheme:orthography:tokenRange:)`](./nslinguistictagger/tag%28for,at,unit,scheme,orthography,tokenrange%29.md),  [`tags(in:unit:scheme:options:tokenRanges:)`](./nslinguistictagger/tags%28in,unit,scheme,options,tokenranges%29.md), and [`enumerateTags(in:unit:scheme:options:using:)`](./nslinguistictagger/enumeratetags%28in,unit,scheme,options,using%29.md) methods.

## Topics

### Constants
- [NSLinguisticTaggerUnit.document](./nslinguistictaggerunit/document.md)
  The document in its entirety.
- [NSLinguisticTaggerUnit.paragraph](./nslinguistictaggerunit/paragraph.md)
  An individual paragraph.
- [NSLinguisticTaggerUnit.sentence](./nslinguistictaggerunit/sentence.md)
  An individual sentence.
- [NSLinguisticTaggerUnit.word](./nslinguistictaggerunit/word.md)
  An individual word.
### Initializers
- [init?(rawValue: Int)](./nslinguistictaggerunit/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting Types
- [struct NSLinguisticTagScheme](./nslinguistictagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
- [struct NSLinguisticTag](./nslinguistictag.md)
  A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictaggerunit)*