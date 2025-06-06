# CTFontDescriptorCreateMatchingFontDescriptors(_:_:)

**Framework**: Core Text  
**Kind**: func

Returns an array of normalized font descriptors matching the provided descriptor.

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
func CTFontDescriptorCreateMatchingFontDescriptors(_ descriptor: CTFontDescriptor, _ mandatoryAttributes: CFSet?) -> CFArray?
```

#### Return Value

A retained array of normalized font descriptors matching the attributes present in `descriptor`.

#### Discussion

If `descriptor` itself is normalized, then the array will contain only one item: the original descriptor. In the context of font descriptors,  infers that the input values were matched up with actual existing fonts, and the descriptors for those existing fonts are the returned normalized descriptors.

## Parameters

- `descriptor`: The font descriptor.
- `mandatoryAttributes`: A set of attribute keys that must be identically matched in any returned font descriptors. May be  .

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
- [func CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor, CFSet?) -> CTFontDescriptor?](ctfontdescriptorcreatematchingfontdescriptor(_:_:).md)
  Returns the single preferred matching font descriptor based on the original descriptor and system precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatematchingfontdescriptors(_:_:))*