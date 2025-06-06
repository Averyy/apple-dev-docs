# dataSource

**Framework**: AppKit  
**Kind**: property

An object that provides data for the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
weak var dataSource: (any NSCollectionViewDataSource)? { get set }
```

#### Discussion

The data source object manages the data in the collection view. Use this object to specify how many items are in the collection view and to create the visual representation of those items. The object you specify must adopt the [`NSCollectionViewDataSource`](nscollectionviewdatasource.md) protocol.

To specify the data for your collection view, assign a value to this property or to the [`content`](nscollectionview/content.md) property, but not both. If you specify a value for this property, the collection view ignores the [`content`](nscollectionview/content.md) property and the `content` binding.

## See Also

- [protocol NSCollectionViewDataSource](nscollectionviewdatasource.md)
  A set of methods that a data source object implements to provide the information and view objects that a collection view requires to present content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/datasource)*