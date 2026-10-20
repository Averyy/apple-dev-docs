# acceptsGlyphInfo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the client handles `NSGlyphInfoAttributeName` or not.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var acceptsGlyphInfo: Bool { get set }
```

```objc
@property BOOL acceptsGlyphInfo;
```

#### Discussion

The default value is determined by examining the return value from sending a `validAttributesForMarkedText` message to the client at initialization.

## See Also

### Configuring the Input Context
- [var allowedInputSourceLocales: [String]?](./allowedinputsourcelocales.md)
  The set of keyboard input source locales allowed when this input context is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputcontext/acceptsglyphinfo)*