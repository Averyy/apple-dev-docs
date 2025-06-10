# fulfill(with:)

**Framework**: CallKit  
**Kind**: method

Reports that the translation action was successful.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
func fulfill(with translationEngine: CXTranslationEngine)
```

## Parameters

- `translationEngine`: A value that indicates whether the translation action used the system’s default translation engine or an external translation engine.

## See Also

- [enum CXTranslationEngine](cxtranslationengine.md)
  Values that describe the translation engine that provided a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxsettranslatingcallaction/fulfill(with:))*