# CTFontDescriptorCreateMatchingFontDescriptor(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns the single preferred matching font descriptor based on the original descriptor and system precedence.

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
func CTFontDescriptorCreateMatchingFontDescriptor(_ descriptor: CTFontDescriptor, _ mandatoryAttributes: CFSet?) -> CTFontDescriptor?
```

#### Return Value

A retained, normalized font descriptor matching the attributes present in `descriptor`.

#### Discussion

The original descriptor may be returned in normalized form. The caller is responsible for releasing the result. In the context of font descriptors,  infers that the input values were matched up with actual existing fonts, and the descriptors for those existing fonts are the returned normalized descriptors.

## Parameters

- `descriptor`: The original font descriptor.
- `mandatoryAttributes`: A set of attribute keys which must be identically matched in any returned font descriptors. May be  .

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
- [func CTFontDescriptorCreateCopyWithFamily(CTFontDescriptor, CFString) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithfamily(_:_:).md)
  Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [func CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithsymbolictraits(_:_:_:).md)
  Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [func CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor, CFSet?) -> CFArray?](ctfontdescriptorcreatematchingfontdescriptors(_:_:).md)
  Returns an array of normalized font descriptors matching the provided descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatematchingfontdescriptor(_:_:))*