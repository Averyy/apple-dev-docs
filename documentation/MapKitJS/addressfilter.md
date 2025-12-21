# AddressFilter

**Framework**: MapKit JS  
**Kind**: class

An object that filters which address options to include or exclude in search results.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
class AddressFilter
```

#### Overview

Use this object to filter search results by criteria, such as country, region, and municipality. See [`AddressCategory`](addresscategory.md) for more information.

## Topics

### Creating filters
- [excluding(categories)](addressfilter/excluding.md)
  A list of categories to exclude from a search.
- [including(categories)](addressfilter/including.md)
  A list of categories to include in a search.
- [excludingAllCategories](addressfilter/excludingallcategories.md)
  A value that excludes all address categories.
- [includingAllCategories](addressfilter/includingallcategories.md)
  A value that includes all address categories.
### Querying filter behavior
- [excludesCategory(category)](addressfilter/excludescategory.md)
  A Boolean value that indicates whether to exclude a category from a search.
- [includesCategory(category)](addressfilter/includescategory.md)
  A Boolean value that indicates whether to include a category from a search.

## See Also

- [const AddressCategory](addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [class Search](search.md)
  An object that retrieves map-based search results for a user-entered query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/addressfilter)*