# asset(for:resultBlock:failureBlock:)

**Framework**: Assets Library  
**Kind**: method

Invokes a given block passing as a parameter an asset identified by a specified file URL.

## Declaration

```swift
func asset(for assetURL: URL!, resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)
```

#### Discussion

This method is asynchronous. When the asset is requested, the user may be asked to confirm the application’s access to the library; the method, though, returns immediately. You should perform whatever work you want with the asset in `resultBlock`.

If the user denies access to the application, or if no application is allowed to access the data, the failure block is called.

## Parameters

- `assetURL`: An asset URL previously retrieved from an [`ALAsset`](alasset.md) object.
- `resultBlock`: The block to invoke using the asset identified by `assetURL`. For a description of the block, see [`ALAssetsLibraryAssetForURLResultBlock`](alassetslibraryassetforurlresultblock.md).
- `failureBlock`: The block to invoke if the user denies access to the assets library. For a description of the block, see [`ALAssetsLibraryAccessFailureBlock`](alassetslibraryaccessfailureblock.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/asset(for:resultblock:failureblock:))*