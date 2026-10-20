# NSFontCollectionMatchingOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These constants are used by the [`matchingDescriptors(options:)`](./nsfontcollection/matchingdescriptors%28options%29.md) and [`matchingDescriptors(forFamily:options:)`](./nsfontcollection/matchingdescriptors%28forfamily,options%29.md) options dictionary parameters.

**Availability**:
- macOS

## Declaration

```swift
struct NSFontCollectionMatchingOptionKey
```

```c
typedef NSString * NSFontCollectionMatchingOptionKey;
```

## Topics

### Type Properties
- [static let includeDisabledFontsOption: NSFontCollectionMatchingOptionKey](./nsfontcollectionmatchingoptionkey/includedisabledfontsoption.md)
  An NSNumber object containing a Boolean value specifying whether disabled fonts should be included in the list of matching descriptors.
- [static let removeDuplicatesOption: NSFontCollectionMatchingOptionKey](./nsfontcollectionmatchingoptionkey/removeduplicatesoption.md)
  An NSNumber object containing a Boolean value controlling whether more than one copy of a font with the same PostScript name should be included in the list of matching descriptors.
- [static let disallowAutoActivationOption: NSFontCollectionMatchingOptionKey](./nsfontcollectionmatchingoptionkey/disallowautoactivationoption.md)
  An NSNumber object containing a Boolean value specifying that auto-activation should not be used to find missing fonts.
### Initializers
- [init(rawValue: String)](./nsfontcollectionmatchingoptionkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Font Descriptors
- [var matchingDescriptors: [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors.md)
  An array of font descriptors matching the logical descriptors.
- [func matchingDescriptors(forFamily: String) -> [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors%28forfamily%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family.
- [func matchingDescriptors(forFamily: String, options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors%28forfamily,options%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family and options.
- [func matchingDescriptors(options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./nsfontcollection/matchingdescriptors%28options%29.md)
  Returns an array of font descriptors matching the logical descriptors with the given options.
- [var queryDescriptors: [NSFontDescriptor]?](./nsfontcollection/querydescriptors.md)
  An array of font descriptors whose matching results produce the collection’s matching descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./nsfontcollection/exclusiondescriptors.md)
  A list of query font descriptors whose matching results are excluded from the list of matching descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollectionmatchingoptionkey)*