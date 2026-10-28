# forAsset()

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a request for adding a new asset to the Photos library using asset resources.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func forAsset() -> Self
```

```objc
+ (instancetype) creationRequestForAsset;
```

## Return Value

An asset creation request.

## Discussion

Call this method within a photo library change block to create a new asset. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md). After calling this method, and before returning from the change block, use [`addResource(with:data:options:)`](./addresource%28with,data,options%29.md) or [`addResource(with:fileURL:options:)`](./addresource%28with,fileurl,options%29.md) to specify one or more data resources for the asset.

To set metadata properties of the newly created asset, use the corresponding properties of the change request (provided by the superclass [`PHAssetChangeRequest`](../phassetchangerequest.md) and listed in Modifying Assets). To reference the newly created asset later in the same change block or after the change block completes, use the [`placeholderForCreatedAsset`](../phassetchangerequest/placeholderforcreatedasset.md) property to retrieve a placeholder object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcreationrequest/forasset())*