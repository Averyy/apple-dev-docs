# group(for:resultBlock:failureBlock:)

**Framework**: Assets Library  
**Kind**: method

Returns an assets group in the result block for a URL previously retrieved from an `ALAssetsGroup` object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func group(for groupURL: URL!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)
```

#### Discussion

This method is asynchronous: it returns immediately. You should perform whatever work you want with the assets group in `resultBlock`.

This method is asynchronous. When the assets group is requested, the user may be asked to confirm the application’s access to the data; the method, though, returns immediately. You should perform whatever work you want with the asset group in `resultBlock`.

If the user denies access to the application, or if no application is allowed to access the data, or if the data is currently unavailable, the failure block is called.

## Parameters

- `groupURL`: The URL for an   object.
- `resultBlock`: For a description of the block, see  .
- `failureBlock`: For a description of the block, see  .

## See Also

- [func addAssetsGroupAlbum(withName: String!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/addassetsgroupalbum(withname:resultblock:failureblock:).md)
  Adds a new assets group to the library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/group(for:resultblock:failureblock:))*