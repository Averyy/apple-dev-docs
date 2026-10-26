# title

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The displayed name of the asset collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var title: String { get set }
```

```objc
@property (nonatomic, strong, readwrite) NSString * title;
```

#### Discussion

Set this property to change the asset collection’s title.

## See Also

### Modifying Asset Collections
- [convenience init?(for: PHAssetCollection)](./init%28for%29.md)
  Creates a request for modifying the specified asset collection.
- [convenience init?(for: PHAssetCollection, assets: PHFetchResult<PHAsset>?)](./init%28for,assets%29.md)
  Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [func addAssets(any NSFastEnumeration)](./addassets%28_%29.md)
  Adds the specified assets to the asset collection.
- [func insertAssets(any NSFastEnumeration, at: IndexSet)](./insertassets%28_,at%29.md)
  Inserts the specified assets into the collection at the specified indexes.
- [func removeAssets(any NSFastEnumeration)](./removeassets%28_%29.md)
  Removes the specified assets from the asset collection.
- [func removeAssets(at: IndexSet)](./removeassets%28at%29.md)
  Removes the assets at the specified indexes from the asset collection.
- [func replaceAssets(at: IndexSet, withAssets: any NSFastEnumeration)](./replaceassets%28at,withassets%29.md)
  Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [func moveAssets(at: IndexSet, to: Int)](./moveassets%28at,to%29.md)
  Moves the assets at the specified indexes in the asset collection to a new index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/title)*