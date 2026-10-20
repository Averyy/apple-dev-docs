# dataSourceIndexPath(forPresentationIndexPath:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Translates an index in your presented layout to the equivalent index in your data source object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func dataSourceIndexPath(forPresentationIndexPath presentationIndexPath: IndexPath?) -> IndexPath?
```

```objc
- (NSIndexPath *) dataSourceIndexPathForPresentationIndexPath:(NSIndexPath *) presentationIndexPath;
```

#### Return Value

The index path of the same item in the data source object, or `nil` if the item is no longer in the data source.

## Parameters

- `presentationIndexPath`: The index path of an item in your presentation layer.

## See Also

### Managing item positions
- [func presentationIndexPath(forDataSourceIndexPath: IndexPath?) -> IndexPath?](./presentationindexpath%28fordatasourceindexpath%29.md)
  Translates an index in your data source object to the equivalent index in your presented layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating/datasourceindexpath(forpresentationindexpath:))*