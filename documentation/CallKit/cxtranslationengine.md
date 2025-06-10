# CXTranslationEngine

**Framework**: CallKit  
**Kind**: enum

Values that describe the translation engine that provided a translation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+

## Declaration

```swift
enum CXTranslationEngine
```

## Topics

### Types
- [CXTranslationEngine.default](cxtranslationengine/default.md)
  The translation was provided by the system’s default translation engine.
- [CXTranslationEngine.external](cxtranslationengine/external.md)
  The translation was provided by an external translation engine.
### Initializers
- [init?(rawValue: UInt)](cxtranslationengine/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fulfill(with: CXTranslationEngine)](cxsettranslatingcallaction/fulfill(with:).md)
  Reports that the translation action was successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtranslationengine)*