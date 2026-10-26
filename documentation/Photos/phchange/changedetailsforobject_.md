# changeDetailsForObject:

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns detailed change information for the specified asset or collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```objc
- (PHObjectChangeDetails *) changeDetailsForObject:(PHObject *) object;
```

#### Return Value

A change details object, or `nil` if there have been no changes to the specified asset or collection.

#### Discussion

When Photos calls your change observer’s [`photoLibraryDidChange(_:)`](../phphotolibrarychangeobserver/photolibrarydidchange%28_%29.md) method, get detailed change information about an asset or collection you’ve previously fetched by calling the `changeDetailsForObject` methods:

- [`changeDetailsForObject:`](./changedetailsforobject_.md)
- [`changeDetails(for:)`](./changedetails%28for%29-536rd.md)
- [`changeDetails(for:)`](./changedetails%28for%29-2fne7.md)

If the asset or collection has changed since you last fetched it, the resulting [`PHObjectChangeDetails`](../phobjectchangedetails.md) object describes the changes. If there are no changes between the fetched object and the current state of the asset or collection it represents in the Photos library, this method returns `nil`.

For an asset collection or collection list, this method and the [`PHObjectChangeDetails`](../phobjectchangedetails.md) object it returns describe changes only to the collection’s properties. If you are instead interested in changes to the collection’s membership, use the [`changeDetails(for:)`](./changedetails%28for%29-33a6n.md) method.

## Parameters

- `object`: A [`PHAsset`](../phasset.md), [`PHAssetCollection`](../phassetcollection.md), or [`PHCollectionList`](../phcollectionlist.md) object.

## See Also

### Getting Change Details
- [- changeDetailsForFetchResult:](./changedetailsforfetchresult_.md)
  Returns detailed change information for a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phchange/changedetailsforobject:)*