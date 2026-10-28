# PHAssetEditOperation.delete

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The asset can be deleted from the photo library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case delete
```

```c
PHAssetEditOperationDelete
```

## Discussion

To delete one or more assets, create a change request with the [`deleteAssets(_:)`](../phassetchangerequest/deleteassets%28_%29.md) method inside a [`PHPhotoLibrary`](../phphotolibrary.md) change block.

## See Also

### Constants
- [PHAssetEditOperation.content](./content.md)
  The asset’s photo or video content can be edited.
- [PHAssetEditOperation.properties](./properties.md)
  The asset’s metadata properties can be edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasseteditoperation/delete)*