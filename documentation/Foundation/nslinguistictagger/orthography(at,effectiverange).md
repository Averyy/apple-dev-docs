# orthography(at:effectiveRange:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the orthography at the index and also returns the effective range.

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
func orthography(at charIndex: Int, effectiveRange: NSRangePointer?) -> NSOrthography?
```

```objc
- (NSOrthography *) orthographyAtIndex:(NSUInteger) charIndex effectiveRange:(NSRangePointer) effectiveRange;
```

## Return Value

The orthography for the location.

## Parameters

- `charIndex`: The character index to begin examination.
- `effectiveRange`: An NSRangePointer that, upon completion, contains the range of the orthography containing `charIndex`.

## See Also

### Determining the Dominant Language and Orthography
- [class func dominantLanguage(for: String) -> String?](./dominantlanguage%28for%29.md)
  Returns the dominant language for the specified string.
- [var dominantLanguage: String?](./dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func setOrthography(NSOrthography?, range: NSRange)](./setorthography%28_,range%29.md)
  Sets the orthography for the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/orthography(at:effectiverange:))*