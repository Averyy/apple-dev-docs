# CTFontDescriptorCreateCopyWithFamily(_:_:)

**Framework**: Core Text  
**Kind**: func

Creates a copy of the font descriptor in the specified family based on the traits of the original.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTFontDescriptorCreateCopyWithFamily(_ original: CTFontDescriptor, _ family: CFString) -> CTFontDescriptor?
```

#### Return Value

A new font descriptor with the original traits in the given family, or `NULL` if no matching font descriptor is found in the system.

## Parameters

- `original`: The original font descriptor.
- `family`: The name of the desired family.

## See Also

- [func CTFontDescriptorCreateWithNameAndSize(CFString, CGFloat) -> CTFontDescriptor](ctfontdescriptorcreatewithnameandsize(_:_:).md)
  Creates a new font descriptor with the provided PostScript name and size.
- [func CTFontDescriptorCreateWithAttributes(CFDictionary) -> CTFontDescriptor](ctfontdescriptorcreatewithattributes(_:).md)
  Creates a new font descriptor reference from a dictionary of attributes.
- [func CTFontDescriptorCreateCopyWithAttributes(CTFontDescriptor, CFDictionary) -> CTFontDescriptor](ctfontdescriptorcreatecopywithattributes(_:_:).md)
  Creates a copy of the original font descriptor with new attributes.
- [func CTFontDescriptorCreateCopyWithVariation(CTFontDescriptor, CFNumber, CGFloat) -> CTFontDescriptor](ctfontdescriptorcreatecopywithvariation(_:_:_:).md)
  Creates a copy of the original font descriptor with a new variation instance.
- [func CTFontDescriptorCreateCopyWithFeature(CTFontDescriptor, CFNumber, CFNumber) -> CTFontDescriptor](ctfontdescriptorcreatecopywithfeature(_:_:_:).md)
  Copies a font descriptor with new feature settings.
- [func CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithsymbolictraits(_:_:_:).md)
  Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [func CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor, CFSet?) -> CFArray?](ctfontdescriptorcreatematchingfontdescriptors(_:_:).md)
  Returns an array of normalized font descriptors matching the provided descriptor.
- [func CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor, CFSet?) -> CTFontDescriptor?](ctfontdescriptorcreatematchingfontdescriptor(_:_:).md)
  Returns the single preferred matching font descriptor based on the original descriptor and system precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatecopywithfamily(_:_:))*