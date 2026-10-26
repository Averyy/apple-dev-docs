# removeAssets(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Removes assets of a certain type from the collection.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func removeAssets<T>(_ assets: T) where T : Collection, T.Element == PHAsset
```

## Parameters

- `assets`: The type of assets to remove from the collection.

## See Also

### Removing Assets
- [func removeAssets(PHFetchResult<PHAsset>)](./removeassets%28_%29-3ytt3.md)
  Removes assets based on a fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phprojectchangerequest/removeassets(_:)-n825)*