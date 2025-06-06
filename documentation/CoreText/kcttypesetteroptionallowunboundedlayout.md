# kCTTypesetterOptionAllowUnboundedLayout

**Framework**: Core Text  
**Kind**: var

A key that specifies whether the text system lays out text that requires unreasonable effort.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let kCTTypesetterOptionAllowUnboundedLayout: CFString
```

#### Discussion

Proper Unicode layout of some text requires unreasonable effort. By default, the text system avoids expending this effort. To create a typesetter that always typesets the text, regardless of the amount of work needed, call [`CTTypesetterCreateWithAttributedStringAndOptions(_:_:)`](cttypesettercreatewithattributedstringandoptions(_:_:).md) and set this option to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).

The value for this key must be a `CFBooleanRef`. The default value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse).

## See Also

- [let kCTTypesetterOptionForcedEmbeddingLevel: CFString](kcttypesetteroptionforcedembeddinglevel.md)
  A key that specifies the embedding level of the typesetter’s text.
- [let kCTTypesetterOptionDisableBidiProcessing: CFString](kcttypesetteroptiondisablebidiprocessing.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kcttypesetteroptionallowunboundedlayout)*