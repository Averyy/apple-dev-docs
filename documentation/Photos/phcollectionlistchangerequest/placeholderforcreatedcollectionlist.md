# placeholderForCreatedCollectionList

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A placeholder object for the collection list that the change request creates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var placeholderForCreatedCollectionList: PHObjectPlaceholder { get }
```

```objc
@property (nonatomic, strong, readonly) PHObjectPlaceholder * placeholderForCreatedCollectionList;
```

#### Discussion

Use this property if you need to reference the collection created by a change request within the same change block. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

## See Also

### Managing Collection Lists
- [class func creationRequestForCollectionList(withTitle: String) -> Self](./creationrequestforcollectionlist%28withtitle%29.md)
  Creates a request for adding a new collection list to the Photos library.
- [class func deleteCollectionLists(any NSFastEnumeration)](./deletecollectionlists%28_%29.md)
  Requests to delete the specified asset collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/placeholderforcreatedcollectionlist)*