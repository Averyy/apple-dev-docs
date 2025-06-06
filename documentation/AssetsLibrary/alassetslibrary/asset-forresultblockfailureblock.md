# asset(for:resultBlock:failureBlock:)

**Framework**: Assets Library  
**Kind**: method

Invokes a given block passing as a parameter an asset identified by a specified file URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func asset(for assetURL: URL!, resultBlock: ALAssetsLibraryAssetForURLResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)
```

#### Discussion

This method is asynchronous. When the asset is requested, the user may be asked to confirm the application’s access to the library; the method, though, returns immediately. You should perform whatever work you want with the asset in `resultBlock`.

If the user denies access to the application, or if no application is allowed to access the data, the failure block is called.

## Parameters

- `assetURL`: An asset URL previously retrieved from an   object.
- `resultBlock`: For a description of the block, see  .
- `failureBlock`: For a description of the block, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/asset(for:resultblock:failureblock:))*