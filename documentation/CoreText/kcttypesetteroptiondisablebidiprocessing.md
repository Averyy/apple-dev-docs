# kCTTypesetterOptionDisableBidiProcessing

**Framework**: Core Text  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 3.2+ - Deprecated in 6.0
- iPadOS 3.2+ - Deprecated in 6.0
- Mac Catalyst 3.2+ - Deprecated in 6.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Deprecated

## Declaration

```swift
let kCTTypesetterOptionDisableBidiProcessing: CFString
```

```c
extern CFStringRef const kCTTypesetterOptionDisableBidiProcessing;
```

## Discussion

Disables bidirectional processing. Value must be a CFBoolean object. Default value is `false`. Normally, typesetting applies the Unicode Bidirectional Algorithm as described in Unicode Standard Annex #9. If a typesetter is created with this option set to `true`, no directional reordering is performed, and any directional control characters are ignored.

## See Also

### Constants
- [let kCTTypesetterOptionForcedEmbeddingLevel: CFString](./kcttypesetteroptionforcedembeddinglevel.md)
  A key that specifies the embedding level of the typesetter’s text.
- [let kCTTypesetterOptionAllowUnboundedLayout: CFString](./kcttypesetteroptionallowunboundedlayout.md)
  A key that specifies whether the text system lays out text that requires unreasonable effort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kcttypesetteroptiondisablebidiprocessing)*