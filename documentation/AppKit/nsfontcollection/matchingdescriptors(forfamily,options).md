# matchingDescriptors(forFamily:options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of font descriptors matching the logical descriptors for the given font family and options.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func matchingDescriptors(forFamily family: String, options: [NSFontCollectionMatchingOptionKey : NSNumber]? = nil) -> [NSFontDescriptor]?
```

```objc
- (NSArray<NSFontDescriptor *> *) matchingDescriptorsForFamily:(NSString *) family options:(NSDictionary<NSString *,NSNumber *> *) options;
```

## Return Value

The [`matchingDescriptors`](./matchingdescriptors.md) for the given family and options.

## Parameters

- `family`: The font family whose descriptors are matched.
- `options`: A dictionary containing any combination of the `Matching Descriptors Options` keys or `nil`.

## See Also

### Getting the Font Descriptors
- [var matchingDescriptors: [NSFontDescriptor]?](./matchingdescriptors.md)
  An array of font descriptors matching the logical descriptors.
- [func matchingDescriptors(forFamily: String) -> [NSFontDescriptor]?](./matchingdescriptors%28forfamily%29.md)
  Returns an array of font descriptors matching the logical descriptors for the given font family.
- [func matchingDescriptors(options: [NSFontCollectionMatchingOptionKey : NSNumber]?) -> [NSFontDescriptor]?](./matchingdescriptors%28options%29.md)
  Returns an array of font descriptors matching the logical descriptors with the given options.
- [struct NSFontCollectionMatchingOptionKey](../nsfontcollectionmatchingoptionkey.md)
  These constants are used by the [`matchingDescriptors(options:)`](./matchingdescriptors%28options%29.md) and [`matchingDescriptors(forFamily:options:)`](./matchingdescriptors%28forfamily,options%29.md) options dictionary parameters.
- [var queryDescriptors: [NSFontDescriptor]?](./querydescriptors.md)
  An array of font descriptors whose matching results produce the collection’s matching descriptors.
- [var exclusionDescriptors: [NSFontDescriptor]?](./exclusiondescriptors.md)
  A list of query font descriptors whose matching results are excluded from the list of matching descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontcollection/matchingdescriptors(forfamily:options:))*