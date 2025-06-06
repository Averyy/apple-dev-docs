# matchingFontDescriptors(withMandatoryKeys:)

**Framework**: UIKit  
**Kind**: method

Returns all the fonts available in the system with specified attributes that match those of the font.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func matchingFontDescriptors(withMandatoryKeys mandatoryKeys: Set<UIFontDescriptor.AttributeName>?) -> [UIFontDescriptor]
```

#### Return Value

The matching font descriptors. If the attribute value specified does not exist in the input dictionary or if there is no font that matches the given mandatory key values, an empty array is returned.

#### Discussion

For example, suppose there are two versions of a given font installed that differ in the number of glyphs covered (the new version has more glyphs). If you explicitly specify `UIFontDescriptorNameAttribute` as the only mandatory key, then a font descriptor that specifies a font name and character set by default matches both versions, because the character set attribute isn’t used for matching. If you specify that font name and character set keys are mandatory, the returned array contains only the font that matches both keys.

## Parameters

- `mandatoryKeys`: Keys that must be identical to be matched. Can be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/matchingfontdescriptors(withmandatorykeys:))*