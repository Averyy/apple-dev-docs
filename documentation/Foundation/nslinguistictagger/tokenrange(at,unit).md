# tokenRange(at:unit:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the range of the linguistic unit containing the specified character index.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 4.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
func tokenRange(at charIndex: Int, unit: NSLinguisticTaggerUnit) -> NSRange
```

```objc
- (NSRange) tokenRangeAtIndex:(NSUInteger) charIndex unit:(NSLinguisticTaggerUnit) unit;
```

#### Return Value

The range of the substring for the linguistic unit.

## Parameters

- `charIndex`: The character index to begin examination.
- `unit`: The linguistic unit. For possible values, see [`NSLinguisticTaggerUnit`](../nslinguistictaggerunit.md).

## See Also

### Determining the Range of a Unit Token
- [func sentenceRange(for: NSRange) -> NSRange](./sentencerange%28for%29.md)
  Returns the range of a sentence containing the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tokenrange(at:unit:))*