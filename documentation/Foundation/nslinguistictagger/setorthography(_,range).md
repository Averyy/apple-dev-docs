# setOrthography(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the orthography for the specified range.

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
func setOrthography(_ orthography: NSOrthography?, range: NSRange)
```

```objc
- (void) setOrthography:(NSOrthography *) orthography range:(NSRange) range;
```

#### Discussion

If the orthography of the linguistic tagger is not set, it will determine it automatically from the contents of the text.  You should call this method only if you  know the orthography of the text by some other means.

## Parameters

- `orthography`: The orthography.
- `range`: The range.

## See Also

### Determining the Dominant Language and Orthography
- [class func dominantLanguage(for: String) -> String?](./dominantlanguage%28for%29.md)
  Returns the dominant language for the specified string.
- [var dominantLanguage: String?](./dominantlanguage.md)
  Returns the dominant language of the string set for the linguistic tagger.
- [func orthography(at: Int, effectiveRange: NSRangePointer?) -> NSOrthography?](./orthography%28at,effectiverange%29.md)
  Returns the orthography at the index and also returns the effective range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/setorthography(_:range:))*