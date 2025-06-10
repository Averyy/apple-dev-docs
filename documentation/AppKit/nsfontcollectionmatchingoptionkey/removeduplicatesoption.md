# removeDuplicatesOption

**Framework**: AppKit  
**Kind**: property

An NSNumber object containing a Boolean value controlling whether more than one copy of a font with the same PostScript name should be included in the list of matching descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let removeDuplicatesOption: NSFontCollectionMatchingOptionKey
```

## See Also

- [static let includeDisabledFontsOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/includedisabledfontsoption.md)
  An NSNumber object containing a Boolean value specifying whether disabled fonts should be included in the list of matching descriptors; [`true`](https://developer.apple.com/documentation/swift/true) if they should be included, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. When unspecified, CoreText assumes [`false`](https://developer.apple.com/documentation/swift/false). This option is intended only for font management applications. This option will make descriptor matching slower.
- [static let disallowAutoActivationOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/disallowautoactivationoption.md)
  An NSNumber object containing a Boolean value specifying that auto-activation should not be used to find missing fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey/removeduplicatesoption)*