# allowedInputSourceLocales

**Framework**: AppKit  
**Kind**: property

The set of keyboard input source locales allowed when this input context is active.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var allowedInputSourceLocales: [String]? { get set }
```

#### Discussion

`NSAllRomanInputSourcesLocaleIdentifier` can be specified as a valid locale.

## See Also

- [var acceptsGlyphInfo: Bool](nstextinputcontext/acceptsglyphinfo.md)
  A Boolean value that indicates whether the client handles `NSGlyphInfoAttributeName` or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/allowedinputsourcelocales)*