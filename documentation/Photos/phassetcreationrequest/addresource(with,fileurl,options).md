# addResource(with:fileURL:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Adds a data resource to the asset being created, using the file at the specified URL.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func addResource(with type: PHAssetResourceType, fileURL: URL, options: PHAssetResourceCreationOptions?)
```

```objc
- (void) addResourceWithType:(PHAssetResourceType) type fileURL:(NSURL *) fileURL options:(PHAssetResourceCreationOptions *) options;
```

#### Discussion

Photos imports the asset resource data only when it executes the [`PHPhotoLibrary`](../phphotolibrary.md) change block in which you create a [`PHAssetCreationRequest`](../phassetcreationrequest.md) object and call this method. If you attempt to create an asset with invalid data or an invalid combination of resources, Photos reports an error in the completion handler of your [`PHPhotoLibrary`](../phphotolibrary.md) call.

## Parameters

- `type`: The role of this data resource in constructing an asset. For details, see [`PHAssetResourceType`](../phassetresourcetype.md).
- `fileURL`: The URL to a local file containing data for the asset resource.
- `options`: Options affecting how Photos constructs the asset resource and incorporates its data into the Photos library. For details, see [`PHAssetResourceCreationOptions`](../phassetresourcecreationoptions.md).

## See Also

### Providing Data Resources for the New Asset
- [func addResource(with: PHAssetResourceType, data: Data, options: PHAssetResourceCreationOptions?)](./addresource%28with,data,options%29.md)
  Adds a data resource to the asset being created, using the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcreationrequest/addresource(with:fileurl:options:))*