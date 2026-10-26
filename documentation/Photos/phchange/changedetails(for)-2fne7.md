# changeDetails(for:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns detailed change information for a fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS

## Declaration

```swift
func changeDetails<T>(for fetchResult: PHFetchResult<T>) -> PHFetchResultChangeDetails<T>? where T : PHObject
```

#### Return Value

A change details object, or `nil` if there have been no changes affecting the fetch result’s contents.

#### Discussion

When Photos calls your change observer’s [`photoLibraryDidChange(_:)`](../phphotolibrarychangeobserver/photolibrarydidchange%28_%29.md) method, call this [`changeDetails(for:)`](./changedetails%28for%29-2fne7.md) method to get detailed change information about the results of a fetch you’ve previously performed. If there have been any changes in the Photos library affecting the fetch, the resulting [`PHFetchResultChangeDetails`](../phfetchresultchangedetails.md) object tells you if any contents in the fetch result have been added, removed, or changed since you fetched it. If there have been no changes since you performed the fetch, this method returns `nil`.

Typically, if your app displays the members of a collection (such as an album or moment), you use a method such as [`fetchAssets(in:options:)`](../phasset/fetchassets%28in,options%29.md) to retrieve those members and then keep the resulting [`PHFetchResult`](../phfetchresult.md) object. You can then pass that fetch result to this method to learn about changes to the collection, such as whether new members have been added to it (and which indexes to insert them at in your UI).

To find out about changes to an object’s properties, such as a collection’s title or an asset’s metadata, use the [`changeDetails(for:)`](./changedetails%28for%29-536rd.md) method.

## Parameters

- `fetchResult`: A Photos fetch result.

## See Also

### Getting Change Details
- [func changeDetails(for: PHFetchResult<AnyObject>) -> PHFetchResultChangeDetails<PHObject>?](./changedetails%28for%29-33a6n.md)
- [func changeDetails<T>(for: T) -> PHObjectChangeDetails<T>?](./changedetails%28for%29-536rd.md)
  Returns detailed change information for the specified asset or collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phchange/changedetails(for:)-2fne7)*