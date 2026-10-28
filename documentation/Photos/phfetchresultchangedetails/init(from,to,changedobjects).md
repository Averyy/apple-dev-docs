# init(from:to:changedObjects:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a change details object that summarizes the differences between two fetch results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(from fromResult: PHFetchResult<ObjectType>, to toResult: PHFetchResult<ObjectType>, changedObjects: [ObjectType])
```

```objc
+ (instancetype) changeDetailsFromFetchResult:(PHFetchResult<PHObject *> *) fromResult toFetchResult:(PHFetchResult<PHObject *> *) toResult changedObjects:(NSArray<PHObject *> *) changedObjects;
```

## Return Value

A change details object.

## Discussion

Typically, you use the [`PHChange`](../phchange.md) class to retrieve [`PHFetchResultChangeDetails`](../phfetchresultchangedetails.md) objects describing any changes that have occurred since you performed a fetch, but you can also use this method to get a change details object that summarizes the difference between two arbitrary [`PHFetchResult`](../phfetchresult.md) objects. In this case, Photos cannot automatically determine when the same objects are present in both fetch results but those objects’ content has changed, so the [`changedIndexes`](./changedindexes.md) and [`changedObjects`](./changedobjects.md) properties are empty.

However, you can use the `changedObjects` parameter to manually note objects as changed. For example, consider a view controller that maintains a base fetch result representing a list of albums, and a transient collection that filters the list according to the user’s search terms. For this workflow, you might use a method like the following:

**Swift**:

```swift
func filteredResult(for fetchResult: PHFetchResult<PHCollection>) -> PHFetchResult<PHCollection> {    var filteredAlbums = [PHCollection]()
    fetchResult.enumerateObjects { collection, _, _ in
        if let title = collection.localizedTitle, let searchText = self.searchBar.text, title.hasPrefix(searchText) {
            filteredAlbums.append(collection)
        }
    }
    let filteredList = PHCollectionList.transientCollectionList(with: filteredAlbums, title: nil)
    return PHCollection.fetchCollections(in: filteredList, options: nil)
}
```

**Objective-C**:

```objc
- (PHFetchResult *)filteredResultForFetchResult:(PHFetchResult *)fetchResult {
    NSMutableArray *filteredAlbums = [NSMutableArray arrayWithCapacity:fetchResult.count];
    for (PHCollection *collection in fetchResult) {
        if ([collection.localizedTitle hasPrefix:self.searchBar.text]) {
            [filteredAlbums addObject:collection];
        }
    }
    PHCollectionList *filteredList = [PHCollectionList transientCollectionListWithCollections:filteredAlbums title:nil];
    return [PHCollection fetchCollectionsInCollectionList:filteredList options:nil];
}
```

Because transient collections are not stored in the photo library, Photos cannot provide change details for fetch results against a transient collection. The [`photoLibraryDidChange(_:)`](../phphotolibrarychangeobserver/photolibrarydidchange%28_%29.md) method provides change details for the base fetch result, which you can use to request change details for the filtered fetch result:

**Swift**:

```swift
func photoLibraryDidChange(_ change: PHChange) {
    // This method may be called on a background queue; use the main queue to update the UI.
    DispatchQueue.main.async {
        guard let fetchResultChangeDetails = change.changeDetails(for: self.baseFetchResult)
            else { return }

        // Get the new base fetch result and filter it to get a new filtered result.
        self.baseFetchResult = fetchResultChangeDetails.fetchResultAfterChanges
        let previousFilteredResult = self.filteredFetchResult!
        self.filteredFetchResult = self.filteredResult(for: self.baseFetchResult)

        // Get the changed objects between the original and new base fetches
        // and use them for marking changes between the filtered fetches.
        let filteredChangeDetails = PHFetchResultChangeDetails(
            from: previousFilteredResult,
            to: self.filteredFetchResult,
            changedObjects: fetchResultChangeDetails.changedObjects)

        // Use the filtered change details to update the UI.
        self.updateView(for: filteredChangeDetails)
    }
}
```

**Objective-C**:

```objc
- (void)photoLibraryDidChange:(PHChange *)changeInstance {
    // This method may be called on a background queue; dispatch to the main queue to update the UI.
    dispatch_async(dispatch_get_main_queue(), ^{
 
        PHFetchResultChangeDetails *fetchResultChangeDetails = [changeInstance changeDetailsForFetchResult:self.baseFetchResult];
        if (fetchResultChangeDetails) {
 
            // Get the new base fetch result and filter it to get a new filtered result.
            self.baseFetchResult = fetchResultChangeDetails.fetchResultAfterChanges;
            PHFetchResult *previousFilteredFetchResult = self.filteredFetchResult;
            self.filteredFetchResult = [self filterFetchResult:self.baseFetchResult];
 
            // Get the changed objects between the original and new base fetches,
            // and use them for marking changes between the filtered fetches.
            NSArray *changedObjects = [fetchResultChangeDetails changedObjects];
            PHFetchResultChangeDetails *filteredChangeDetails = [PHFetchResultChangeDetails changeDetailsFromFetchResult:previousFilteredFetchResult toFetchResult:self.filteredFetchResult changedObjects:changedObjects];
 
            // Use the filtered change details to update the UI.
            [self updateViewForChangeDetails:filteredChangeDetails];
        }
    });
}
```

Because you provide the [`changedObjects`](./changedobjects.md) array from the original change details when calling the [`init(from:to:changedObjects:)`](./init%28from,to,changedobjects%29.md) method, Photos can provide a summary of differences between the filtered fetch results that includes [`changedIndexes`](./changedindexes.md) and [`changedObjects`](./changedobjects.md) information. You can then use this information for efficiently updating your app’s interface — for an example of how to do this, see [`PHPhotoLibraryChangeObserver`](../phphotolibrarychangeobserver.md).

## Parameters

- `fromResult`: A fetch result to be treated as the “before” state in the resulting change details object.
- `toResult`: A fetch result to be treated as the “after” state in the resulting change details object.
- `changedObjects`: An collection of objects to manually note as changed between the two fetch results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresultchangedetails/init(from:to:changedobjects:))*