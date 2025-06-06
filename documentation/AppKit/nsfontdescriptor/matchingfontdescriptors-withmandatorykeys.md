# matchingFontDescriptors(withMandatoryKeys:)

**Framework**: AppKit  
**Kind**: method

Returns all the fonts available on the system whose specified attributes match those of the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func matchingFontDescriptors(withMandatoryKeys mandatoryKeys: Set<NSFontDescriptor.AttributeName>?) -> [NSFontDescriptor]
```

#### Return Value

The matching font descriptors. If the attribute value specified does not exist in the input dictionary or if there is no font that matches the given mandatory key values, an empty array is returned.

#### Discussion

For example, suppose there are two versions of a given font installed that differ in the number of glyphs covered (the new version has more glyphs). If you explicitly specify [`name`](nsfontdescriptor/attributename/name.md) as the only mandatory key, then a font descriptor that specifies a font name and character set by default matches both versions, since the character set attribute is not used for matching. If you specify that font name and character set keys are mandatory, the returned array contains only the font that matches both keys.

## Parameters

- `mandatoryKeys`: Keys that must be identical to be matched. Can be  .

## See Also

- [func matchingFontDescriptor(withMandatoryKeys: Set<NSFontDescriptor.AttributeName>?) -> NSFontDescriptor?](nsfontdescriptor/matchingfontdescriptor(withmandatorykeys:).md)
  Returns a normalized font descriptor whose specified attributes match those of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/matchingfontdescriptors(withmandatorykeys:))*