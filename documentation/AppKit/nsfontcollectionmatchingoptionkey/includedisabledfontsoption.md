# includeDisabledFontsOption

**Framework**: AppKit  
**Kind**: property

An NSNumber object containing a Boolean value specifying whether disabled fonts should be included in the list of matching descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let includeDisabledFontsOption: NSFontCollectionMatchingOptionKey
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) indicates they should be included. When unspecified, CoreText assumes [`false`](https://developer.apple.com/documentation/Swift/false). This option is intended only for font management applications. This option will make descriptor matching slower.

## See Also

- [static let removeDuplicatesOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/removeduplicatesoption.md)
  An NSNumber object containing a Boolean value controlling whether more than one copy of a font with the same PostScript name should be included in the list of matching descriptors.
- [static let disallowAutoActivationOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/disallowautoactivationoption.md)
  An NSNumber object containing a Boolean value specifying that auto-activation should not be used to find missing fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey/includedisabledfontsoption)*