# CTFontDescriptorCreateCopyWithFeature(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Copies a font descriptor with new feature settings.

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
func CTFontDescriptorCreateCopyWithFeature(_ original: CTFontDescriptor, _ featureTypeIdentifier: CFNumber, _ featureSelectorIdentifier: CFNumber) -> CTFontDescriptor
```

#### Return Value

A copy of the original font descriptor modified with the given feature settings.

#### Discussion

This is a convenience method to toggle more easily the state of individual features.

## Parameters

- `original`: The original font descriptor.
- `featureTypeIdentifier`: The feature type identifier.
- `featureSelectorIdentifier`: The feature selector identifier.

## See Also

- [func CTFontDescriptorCreateWithNameAndSize(CFString, CGFloat) -> CTFontDescriptor](ctfontdescriptorcreatewithnameandsize(_:_:).md)
  Creates a new font descriptor with the provided PostScript name and size.
- [func CTFontDescriptorCreateWithAttributes(CFDictionary) -> CTFontDescriptor](ctfontdescriptorcreatewithattributes(_:).md)
  Creates a new font descriptor reference from a dictionary of attributes.
- [func CTFontDescriptorCreateCopyWithAttributes(CTFontDescriptor, CFDictionary) -> CTFontDescriptor](ctfontdescriptorcreatecopywithattributes(_:_:).md)
  Creates a copy of the original font descriptor with new attributes.
- [func CTFontDescriptorCreateCopyWithVariation(CTFontDescriptor, CFNumber, CGFloat) -> CTFontDescriptor](ctfontdescriptorcreatecopywithvariation(_:_:_:).md)
  Creates a copy of the original font descriptor with a new variation instance.
- [func CTFontDescriptorCreateCopyWithFamily(CTFontDescriptor, CFString) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithfamily(_:_:).md)
  Creates a copy of the font descriptor in the specified family based on the traits of the original.
- [func CTFontDescriptorCreateCopyWithSymbolicTraits(CTFontDescriptor, CTFontSymbolicTraits, CTFontSymbolicTraits) -> CTFontDescriptor?](ctfontdescriptorcreatecopywithsymbolictraits(_:_:_:).md)
  Creates a copy of the font descriptor with the specified symbolic traits as the original.
- [func CTFontDescriptorCreateMatchingFontDescriptors(CTFontDescriptor, CFSet?) -> CFArray?](ctfontdescriptorcreatematchingfontdescriptors(_:_:).md)
  Returns an array of normalized font descriptors matching the provided descriptor.
- [func CTFontDescriptorCreateMatchingFontDescriptor(CTFontDescriptor, CFSet?) -> CTFontDescriptor?](ctfontdescriptorcreatematchingfontdescriptor(_:_:).md)
  Returns the single preferred matching font descriptor based on the original descriptor and system precedence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontdescriptorcreatecopywithfeature(_:_:_:))*