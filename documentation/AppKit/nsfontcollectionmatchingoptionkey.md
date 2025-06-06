# NSFontCollectionMatchingOptionKey

**Framework**: AppKit  
**Kind**: struct

These constants are used by the [`matchingDescriptors(options:)`](nsfontcollection/matchingdescriptors(options:).md) and [`matchingDescriptors(forFamily:options:)`](nsfontcollection/matchingdescriptors(forfamily:options:).md) options dictionary parameters.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSFontCollectionMatchingOptionKey
```

## Topics

### Type Properties
- [static let includeDisabledFontsOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/includedisabledfontsoption.md)
  An NSNumber object containing a Boolean value specifying whether disabled fonts should be included in the list of matching descriptors; [`true`](https://developer.apple.com/documentation/swift/true) if they should be included, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. When unspecified, CoreText assumes [`false`](https://developer.apple.com/documentation/swift/false). This option is intended only for font management applications. This option will make descriptor matching slower.
- [static let removeDuplicatesOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/removeduplicatesoption.md)
  An NSNumber object containing a Boolean value controlling whether more than one copy of a font with the same PostScript name should be included in the list of matching descriptors.
- [static let disallowAutoActivationOption: NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey/disallowautoactivationoption.md)
  An NSNumber object containing a Boolean value specifying that auto-activation should not be used to find missing fonts.
### Initializers
- [init(rawValue: String)](nsfontcollectionmatchingoptionkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var matchingDescriptors: [NSFontDescriptor]?](nsfontcollection/matchingdescriptors.md)
  An array of font descriptors matching the logical descriptors.
- [func matchingDescriptors(forFamily: String) -> [NSFontDescriptor]?](nsfontcollection/matchingdescriptors(forfamily:).md)
  Returns an array of font descriptors matching the logical descriptors for the given font family.
- [func matchingDescriptors(forFamily: String, options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](nsfontcollection/matchingdescriptors(forfamily:options:).md)
  Returns an array of font descriptors matching the logical descriptors for the given font family and options.
- [func matchingDescriptors(options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](nsfontcollection/matchingdescriptors(options:).md)
  Returns an array of font descriptors matching the logical descriptors with the given options.
- [var queryDescriptors: [NSFontDescriptor]?](nsfontcollection/querydescriptors.md)
  An array of font descriptors whose matching results produce the collection’s matching descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](nsfontcollection/exclusiondescriptors.md)
  A list of query font descriptors whose matching results are excluded from the list of matching descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey)*