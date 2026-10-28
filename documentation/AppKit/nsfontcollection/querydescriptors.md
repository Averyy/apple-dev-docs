# queryDescriptors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of font descriptors whose matching results produce the collection’s matching descriptors.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var queryDescriptors: [NSFontDescriptor]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSFontDescriptor *> * queryDescriptors;
```

## Discussion

The font descriptors matching [`exclusionDescriptors`](./exclusiondescriptors.md) are removed from [`matchingDescriptors`](./matchingdescriptors.md)

## See Also

### Getting the Font Descriptors
- [var matchingDescriptors: [NSFontDescriptor]?](./matchingdescriptors.md)
  An array of font descriptors matching the logical descriptors.
- [func matchingDescriptors(forFamily: String) -> [NSFontDescriptor]?](./matchingdescriptors%28forfamily%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family.
- [func matchingDescriptors(forFamily: String, options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./matchingdescriptors%28forfamily,options%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family and options.
- [func matchingDescriptors(options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./matchingdescriptors%28options%29.md)
  Returns an array of font descriptors matching the logical descriptors with the given options.
- [struct NSFontCollectionMatchingOptionKey](../nsfontcollectionmatchingoptionkey.md)
  These constants are used by the [`matchingDescriptors(options:)`](./matchingdescriptors%28options%29.md) and [`matchingDescriptors(forFamily:options:)`](./matchingdescriptors%28forfamily,options%29.md) options dictionary parameters.
- [var exclusionDescriptors: [NSFontDescriptor]?](./exclusiondescriptors.md)
  A list of query font descriptors whose matching results are excluded from the list of matching descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/querydescriptors)*