# exclusionDescriptors

**Framework**: AppKit  
**Kind**: property

A list of query font descriptors whose matching results are excluded from the list of matching descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var exclusionDescriptors: [NSFontDescriptor]? { get }
```

## See Also

- [var matchingDescriptors: [NSFontDescriptor]?](nsfontcollection/matchingdescriptors.md)
  An array of font descriptors matching the logical descriptors.
- [func matchingDescriptors(forFamily: String) -> [NSFontDescriptor]?](nsfontcollection/matchingdescriptors(forfamily:).md)
  Returns an array of font descriptors matching the logical descriptors for the given font family.
- [func matchingDescriptors(forFamily: String, options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](nsfontcollection/matchingdescriptors(forfamily:options:).md)
  Returns an array of font descriptors matching the logical descriptors for the given font family and options.
- [func matchingDescriptors(options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](nsfontcollection/matchingdescriptors(options:).md)
  Returns an array of font descriptors matching the logical descriptors with the given options.
- [struct NSFontCollectionMatchingOptionKey](nsfontcollectionmatchingoptionkey.md)
  These constants are used by the [`matchingDescriptors(options:)`](nsfontcollection/matchingdescriptors(options:).md) and [`matchingDescriptors(forFamily:options:)`](nsfontcollection/matchingdescriptors(forfamily:options:).md) options dictionary parameters.
- [var queryDescriptors: [NSFontDescriptor]?](nsfontcollection/querydescriptors.md)
  An array of font descriptors whose matching results produce the collection’s matching descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/exclusiondescriptors)*