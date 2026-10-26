# PHAssetEditOperation.properties

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The asset’s metadata properties can be edited.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case properties
```

```c
PHAssetEditOperationProperties
```

#### Discussion

To change an asset’s properties, create a change request with the [`init(for:)`](../phassetchangerequest/init%28for%29.md) method inside a [`PHPhotoLibrary`](../phphotolibrary.md) change block.

## See Also

### Constants
- [PHAssetEditOperation.delete](./delete.md)
  The asset can be deleted from the photo library.
- [PHAssetEditOperation.content](./content.md)
  The asset’s photo or video content can be edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasseteditoperation/properties)*