# presentationIndexPath(forDataSourceIndexPath:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Translates an index in your data source object to the equivalent index in your presented layout.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationIndexPath(forDataSourceIndexPath dataSourceIndexPath: IndexPath?) -> IndexPath?
```

#### Return Value

The index path of the same item in the presentation layer of your object, or `nil` if the item is not in the presentation layer.

## Parameters

- `dataSourceIndexPath`: The index path of an item in the data source object.

## See Also

- [func dataSourceIndexPath(forPresentationIndexPath: IndexPath?) -> IndexPath?](uidatasourcetranslating/datasourceindexpath(forpresentationindexpath:).md)
  Translates an index in your presented layout to the equivalent index in your data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating/presentationindexpath(fordatasourceindexpath:))*