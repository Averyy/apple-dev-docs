# kCTTypesetterOptionDisableBidiProcessing

**Framework**: Core Text  
**Kind**: var

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTTypesetterOptionDisableBidiProcessing: CFString
```

#### Discussion

Disables bidirectional processing. Value must be a CFBoolean object. Default value is `false`. Normally, typesetting applies the Unicode Bidirectional Algorithm as described in Unicode Standard Annex #9. If a typesetter is created with this option set to `true`, no directional reordering is performed, and any directional control characters are ignored.

## See Also

- [let kCTTypesetterOptionForcedEmbeddingLevel: CFString](kcttypesetteroptionforcedembeddinglevel.md)
  A key that specifies the embedding level of the typesetter’s text.
- [let kCTTypesetterOptionAllowUnboundedLayout: CFString](kcttypesetteroptionallowunboundedlayout.md)
  A key that specifies whether the text system lays out text that requires unreasonable effort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kcttypesetteroptiondisablebidiprocessing)*