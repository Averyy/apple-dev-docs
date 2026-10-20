# filterNames(inCategory:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns an array of all published filter names in the specified category.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
class func filterNames(inCategory category: String?) -> [String]
```

```objc
+ (NSArray<NSString *> *) filterNamesInCategory:(NSString *) category;
```

#### Return Value

An array that contains all published names of the filter in a category.

## Parameters

- `category`: A string object that specifies one of the filter categories defined in [Filter Category Keys](../filter-category-keys.md).

## See Also

### Accessing registered filters
- [class func filterNames(inCategories: [String]?) -> [String]](./filternames%28incategories%29.md)
  Returns an array of all published filter names that match all the specified categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filternames(incategory:))*