# presentationIndexPath(forDataSourceIndexPath:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
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
func presentationIndexPath(forDataSourceIndexPath dataSourceIndexPath: IndexPath?) -> IndexPath?
```

```objc
- (NSIndexPath *) presentationIndexPathForDataSourceIndexPath:(NSIndexPath *) dataSourceIndexPath;
```

#### Return Value

The index path of the same item in the presentation layer of your object, or `nil` if the item is not in the presentation layer.

## Parameters

- `dataSourceIndexPath`: The index path of an item in the data source object.

## See Also

### Managing item positions
- [func dataSourceIndexPath(forPresentationIndexPath: IndexPath?) -> IndexPath?](./datasourceindexpath%28forpresentationindexpath%29.md)
  Translates an index in your presented layout to the equivalent index in your data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating/presentationindexpath(fordatasourceindexpath:))*