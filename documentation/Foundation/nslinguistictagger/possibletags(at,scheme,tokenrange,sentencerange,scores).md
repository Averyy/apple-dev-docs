# possibleTags(at:scheme:tokenRange:sentenceRange:scores:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns an array of possible tags for the given scheme at the specified range, supplying matching scores.

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
func possibleTags(at charIndex: Int, scheme tagScheme: String, tokenRange: NSRangePointer?, sentenceRange: NSRangePointer?, scores: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [String]?
```

```objc
- (NSArray<NSString *> *) possibleTagsAtIndex:(NSUInteger) charIndex scheme:(NSString *) tagScheme tokenRange:(NSRangePointer) tokenRange sentenceRange:(NSRangePointer) sentenceRange scores:(NSArray<NSValue *> **) scores;
```

## Return Value

Returns an array of possible tags for the tag scheme at the specified location, starting with the most likely tag scheme.  For some tag schemes only a single tag will be returned, but for others a list of possibilities will be provided.

## Discussion

Calling this method is not recommended; for most use cases, this information is not as useful as what is provided by the methods described in Enumerating Linguistic Tags and Getting Linguistic Tags.

## Parameters

- `charIndex`: The position of the initial character.
- `tagScheme`: The tag scheme. See [`NSLinguisticTagScheme`](../nslinguistictagscheme.md) for possible values.
- `tokenRange`: The token range.
- `sentenceRange`: The range of the sentence.
- `scores`: Returns by reference an array of numeric scores indicating the likelihood that the range matches the tag scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/possibletags(at:scheme:tokenrange:sentencerange:scores:))*