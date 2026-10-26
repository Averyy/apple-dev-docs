# init(forTopLevelCollectionListUserCollections:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request to add, remove, or rearrange child collections in the top-level collection list.

**Availability**:
- iOS 14.2+
- iPadOS 14.2+
- Mac Catalyst 14.2+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(forTopLevelCollectionListUserCollections childCollections: PHFetchResult<PHCollection>)
```

```objc
+ (instancetype) changeRequestForTopLevelCollectionListUserCollections:(PHFetchResult<__kindof PHCollection *> *) childCollections;
```

## Parameters

- `childCollections`: The child collections to modify.

## See Also

### Creating a Change Request
- [convenience init?(for: PHCollectionList)](./init%28for%29.md)
  Creates a request for modifying the specified collection list.
- [convenience init?(for: PHCollectionList, childCollections: PHFetchResult<PHCollection>)](./init%28for,childcollections%29.md)
  Creates a request for modifying the specified collection list, with a fetch result for tracking changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/init(fortoplevelcollectionlistusercollections:))*