# orthographyCheckingResult(range:orthography:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a text checking result with the specified orthography.

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
class func orthographyCheckingResult(range: NSRange, orthography: NSOrthography) -> NSTextCheckingResult
```

```objc
+ (NSTextCheckingResult *) orthographyCheckingResultWithRange:(NSRange) range orthography:(NSOrthography *) orthography;
```

#### Return Value

Returns an `NSTextCheckingResult` with the specified [`range`](./range.md) and a [`resultType`](./resulttype.md) of [`orthography`](./checkingtype/orthography.md).

## Parameters

- `range`: The range of the detected result.
- `orthography`: An orthography object that describes the script.

## See Also

### Text Checking Results for Orthography
- [var orthography: NSOrthography?](./orthography.md)
  The detected orthography of a type checking result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/orthographycheckingresult(range:orthography:))*