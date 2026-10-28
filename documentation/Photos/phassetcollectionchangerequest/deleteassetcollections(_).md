# deleteAssetCollections(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Requests that the specified asset collections be deleted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func deleteAssetCollections(_ assetCollections: any NSFastEnumeration)
```

```objc
+ (void) deleteAssetCollections:(id<NSFastEnumeration>) assetCollections;
```

## Discussion

Call this method within a photo library change block to delete asset collections. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

## Parameters

- `assetCollections`: An array of [`PHAssetCollection`](../phassetcollection.md) objects to be deleted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/deleteassetcollections(_:))*