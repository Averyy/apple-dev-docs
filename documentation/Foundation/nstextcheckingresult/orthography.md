# orthography

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The detected orthography of a type checking result.

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
@NSCopying
var orthography: NSOrthography? { get }
```

```objc
@property (copy, readonly, nullable) NSOrthography * orthography;
```

## See Also

### Text Checking Results for Orthography
- [class func orthographyCheckingResult(range: NSRange, orthography: NSOrthography) -> NSTextCheckingResult](./orthographycheckingresult%28range,orthography%29.md)
  Creates and returns a text checking result with the specified orthography.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nstextcheckingresult/orthography)*