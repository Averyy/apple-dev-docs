# CTFontDescriptorCopyLocalizedAttribute(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Returns a localized value for the requested attribute, if available.

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
func CTFontDescriptorCopyLocalizedAttribute(_ descriptor: CTFontDescriptor, _ attribute: CFString, _ language: UnsafeMutablePointer<Unmanaged<CFString>?>?) -> CFTypeRef?
```

#### Return Value

A retained reference to a localized attribute based on the global language list.

#### Discussion

This function passes back the matched language in `language`. If localization is not possible for the attribute, the behavior matches the value returned from [`CTFontDescriptorCopyAttribute(_:_:)`](ctfontdescriptorcopyattribute(_:_:).md). Generally, localization of attributes is applicable to name attributes of only a normalized font descriptor.

## Parameters

- `descriptor`: The font descriptor.
- `attribute`: The requested font attribute.
- `language`: On output, contains a reference to the matched language. The language identifier will conform to the RFC 3066bis standard.

## See Also

- [func CTFontDescriptorCopyAttributes(CTFontDescriptor) -> CFDictionary](ctfontdescriptorcopyattributes(_:).md)
  Returns the attributes dictionary of the font descriptor.
- [func CTFontDescriptorCopyAttribute(CTFontDescriptor, CFString) -> CFTypeRef?](ctfontdescriptorcopyattribute(_:_:).md)
  Returns the value associated with an arbitrary attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcopylocalizedattribute(_:_:_:))*