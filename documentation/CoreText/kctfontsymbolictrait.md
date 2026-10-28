# kCTFontSymbolicTrait

**Framework**: Core Text  
**Kind**: var  
**Role**: Global Variable

The symbolic traits value from the font traits dictionary.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTFontSymbolicTrait: CFString
```

```c
extern CFStringRef const kCTFontSymbolicTrait;
```

## Discussion

The value is returned as a [`CFNumber`](../CoreFoundation/cfnumber.md) object.

## See Also

### Related Documentation
- [struct CTFontSymbolicTraits](./ctfontsymbolictraits.md)
  The symbolic representation of stylistic font attributes.
### Font Trait Keys
- [let kCTFontWeightTrait: CFString](./kctfontweighttrait.md)
  The normalized weight trait from the font traits dictionary.
- [let kCTFontWidthTrait: CFString](./kctfontwidthtrait.md)
  The normalized proportion (width condense or expand) trait from the font traits dictionary.
- [let kCTFontSlantTrait: CFString](./kctfontslanttrait.md)
  The normalized slant angle from the font traits dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctfontsymbolictrait)*