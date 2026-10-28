# allowedInputSourceLocales

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The set of keyboard input source locales allowed when this input context is active.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var allowedInputSourceLocales: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * allowedInputSourceLocales;
```

## Discussion

`NSAllRomanInputSourcesLocaleIdentifier` can be specified as a valid locale.

## See Also

### Configuring the Input Context
- [var acceptsGlyphInfo: Bool](./acceptsglyphinfo.md)
  A Boolean value that indicates whether the client handles `NSGlyphInfoAttributeName` or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/allowedinputsourcelocales)*