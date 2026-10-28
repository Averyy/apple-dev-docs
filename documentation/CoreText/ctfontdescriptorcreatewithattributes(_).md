# CTFontDescriptorCreateWithAttributes(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates a new font descriptor reference from a dictionary of attributes.

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
func CTFontDescriptorCreateWithAttributes(_ attributes: CFDictionary) -> CTFontDescriptor
```

```c
extern CTFontDescriptorRefCTFontDescriptorCreateWithAttributes(CFDictionaryRef attributes);
```

## Return Value

A new font descriptor with the attributes specified.

## Discussion

The provided attribute dictionary can contain arbitrary attributes that are preserved; however, unrecognized attributes are ignored on font creation and may not be preserved over the round trip from descriptor to font and back to descriptor.

## Parameters

- `attributes`: A dictionary containing arbitrary attributes.

## See Also

### Creating Font Descriptors
- [func CTFontDescriptorCreateWithNameAndSize(CFString, CGFloat) -> CTFontDescriptor](./ctfontdescriptorcreatewithnameandsize%28_,_%29.md)
  Creates a new font descriptor with the provided PostScript name and size.
- [func CTFontDescriptorCreateCopyWithAttributes(CTFontDescriptor, CFDictionary) -> CTFontDescriptor](./ctfontdescriptorcreatecopywithattributes%28_,_%29.md)
  Creates a copy of the original font descriptor with new attributes.
- [func CTFontDescriptorCreateCopyWithVariation(CTFontDescriptor, CFNumber, CGFloat) -> CTFontDescriptor](./ctfontdescriptorcreatecopywithvariation%28_,_,_%29.md)
  Creates a copy of the original font descriptor with a new variation instance.
- [func CTFontDescriptorCreateCopyWithFeature(CTFontDescriptor, CFNumber, CFNumber) -> CTFontDescriptor](./ctfontdescriptorcreatecopywithfeature%28_,_,_%29.md)
  Copies a font descriptor with new feature settings.
- [func CTFontDescriptorCreateCopyWithFamily(CTFontDescriptor, CFString) -> CTFontDescriptor?](./ctfontdescriptorcreatecopywithfamily%28_,_%29.md)
  Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [func CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor?](./ctfontdescriptorcreatecopywithsymbolictraits%28_,_,_%29.md)
  Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [func CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor, CFSet?) -> CFArray?](./ctfontdescriptorcreatematchingfontdescriptors%28_,_%29.md)
  Returns an array of normalized font descriptors matching the provided descriptor.
- [func CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor, CFSet?) -> CTFontDescriptor?](./ctfontdescriptorcreatematchingfontdescriptor%28_,_%29.md)
  Returns the single preferred matching font descriptor based on the original descriptor and system precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatewithattributes(_:))*