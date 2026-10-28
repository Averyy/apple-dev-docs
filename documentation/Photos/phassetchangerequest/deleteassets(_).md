# deleteAssets(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Requests that the specified assets be deleted.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func deleteAssets(_ assets: any NSFastEnumeration)
```

```objc
+ (void) deleteAssets:(id<NSFastEnumeration>) assets;
```

## Discussion

Call this method within a photo library change block to delete assets. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

## Parameters

- `assets`: An array of [`PHAsset`](../phasset.md) objects to be deleted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/deleteassets(_:))*