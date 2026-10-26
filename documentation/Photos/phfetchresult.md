# PHFetchResult

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An ordered list of assets or collections returned from a Photos fetch method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHFetchResult<ObjectType> where ObjectType : AnyObject
```

```objc
@interface PHFetchResult : NSObject
```

## Mentions

- [Uploading asset resources in the background](../PhotoKit/uploading-asset-resources-in-the-background.md)

#### Overview

When you use class methods on the [`PHAsset`](./phasset.md), [`PHCollection`](./phcollection.md), [`PHAssetCollection`](./phassetcollection.md), and [`PHCollectionList`](./phcollectionlist.md) classes to retrieve objects, Photos provides the resulting objects in a fetch result. You access the contents of a fetch result with the same methods and conventions used by the [`NSArray`](../Foundation/nsarray.md) class. Unlike an [`NSArray`](../Foundation/nsarray.md) object, however, a [`PHFetchResult`](./phfetchresult.md) object dynamically loads its contents from the Photos library as needed, providing optimal performance even when handling a large number of results.

A fetch result provides thread-safe access to its contents. After a fetch, the fetch result’s [`count`](./phfetchresult/count.md) value is constant, and all objects in the fetch result keep the same [`localIdentifier`](./phobject/localidentifier.md) value. (To get updated content for a fetch, register a change observer with the shared [`PHPhotoLibrary`](./phphotolibrary.md) object.)

A fetch result caches its contents, keeping a batch of objects around the most recently accessed index. Because objects outside of the batch are no longer cached, accessing these objects results in refetching those objects. This process can result in changes to values previously read from those objects.

## Topics

### Querying a Fetch Result
- [func contains(ObjectType) -> Bool](./phfetchresult/contains%28_%29.md)
  Returns whether the specified object is present in the fetch result.
- [var count: Int](./phfetchresult/count.md)
  The number of objects in the fetch result.
- [func countOfAssets(with: PHAssetMediaType) -> Int](./phfetchresult/countofassets%28with%29.md)
  Returns the number of assets in the fetch result of a specified type.
- [var firstObject: ObjectType?](./phfetchresult/firstobject.md)
  The first object in the fetch result.
- [var lastObject: ObjectType?](./phfetchresult/lastobject.md)
  The last object in the fetch result.
- [func object(at: Int) -> ObjectType](./phfetchresult/object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> ObjectType](./phfetchresult/subscript%28_%29.md)
  Returns the object located at the specified index.
- [func objects(at: IndexSet) -> [ObjectType]](./phfetchresult/objects%28at%29.md)
  Returns an array containing the objects in the fetch result at the indexes in the specified index set.
### Finding Objects in a Fetch Result
- [func index(of: ObjectType) -> Int](./phfetchresult/index%28of%29.md)
  Returns the lowest index whose corresponding object in the fetch result is equal to the specified object.
- [func index(of: ObjectType, in: NSRange) -> Int](./phfetchresult/index%28of,in%29.md)
  Returns the lowest index within the specified range whose corresponding object in the fetch result is equal to the specified object.
### Performing Operations with Objects in a Fetch Result
- [func enumerateObjects(at: IndexSet, options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./phfetchresult/enumerateobjects%28at,options,using%29.md)
  Executes the specified block using the objects in the fetch result at the specified indexes.
- [func enumerateObjects((ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./phfetchresult/enumerateobjects%28_%29.md)
  Executes the specified block using each object in the fetch result, starting with the first object and continuing in order to the last object.
- [func enumerateObjects(options: NSEnumerationOptions, using: (ObjectType, Int, UnsafeMutablePointer<ObjCBool>) -> Void)](./phfetchresult/enumerateobjects%28options,using%29.md)
  Executes the specified block using each object in the fetch result.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSFastEnumeration](../Foundation/nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset retrieval
- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
  Get assets, asset collections, and collection lists matching a specified query.
- [class PHAsset](./phasset.md)
  A representation of an image, video, or Live Photo in the Photos library.
- [class PHAssetCollection](./phassetcollection.md)
  A representation of a Photos asset grouping, such as Moments, a user-created album, or a Smart Album.
- [class PHCollection](./phcollection.md)
  The abstract superclass for Photos asset collections and collection lists.
- [class PHCollectionList](./phcollectionlist.md)
  A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [class PHObject](./phobject.md)
  The abstract superclass for Photos model objects, including assets and collections.
- [class PHFetchOptions](./phfetchoptions.md)
  A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult)*