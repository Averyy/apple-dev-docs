# filterNames(inCategories:)

**Framework**: Core Image  
**Kind**: method

Returns an array of all published filter names that match all the specified categories.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
class func filterNames(inCategories categories: [String]?) -> [String]
```

#### Return Value

An array that contains all published filter names that match all the categories specified by the `categories` argument.

#### Discussion

When you pass more than one filter category, this method returns the intersection of the filters in the categories. For example, if you pass the categories [`kCICategoryBuiltIn`](kcicategorybuiltin.md)  and [`kCICategoryColorAdjustment`](kcicategorycoloradjustment.md), you obtain all the filters that are members of both the built-in and color adjustment categories. But if you pass in `kCICategoryGenerator` and [`kCICategoryStylize`](kcicategorystylize.md), you will not get any filters returned to you because there are no filters that are members of both the generator and stylize categories. If you want to obtain all stylize and generator filters, you must call the `filterNamesInCategories:` method for each category separately and then merge the results.

## Parameters

- `categories`: One or more of the filter category keys defined in  . Pass   to get all filters in all categories.

## See Also

- [class func filterNames(inCategory: String?) -> [String]](cifilter-swift.class/filternames(incategory:).md)
  Returns an array of all published filter names in the specified category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/filternames(incategories:))*