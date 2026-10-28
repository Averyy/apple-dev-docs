# includeDisabledFontsOption

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An NSNumber object containing a Boolean value specifying whether disabled fonts should be included in the list of matching descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let includeDisabledFontsOption: NSFontCollectionMatchingOptionKey
```

```c
extern NSFontCollectionMatchingOptionKey const NSFontCollectionIncludeDisabledFontsOption;
```

## Discussion

[`true`](../../Swift/true.md) indicates they should be included. When unspecified, CoreText assumes [`false`](../../Swift/false.md). This option is intended only for font management applications. This option will make descriptor matching slower.

## See Also

### Type Properties
- [static let removeDuplicatesOption: NSFontCollectionMatchingOptionKey](./removeduplicatesoption.md)
  An NSNumber object containing a Boolean value controlling whether more than one copy of a font with the same PostScript name should be included in the list of matching descriptors.
- [static let disallowAutoActivationOption: NSFontCollectionMatchingOptionKey](./disallowautoactivationoption.md)
  An NSNumber object containing a Boolean value specifying that auto-activation should not be used to find missing fonts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey/includedisabledfontsoption)*