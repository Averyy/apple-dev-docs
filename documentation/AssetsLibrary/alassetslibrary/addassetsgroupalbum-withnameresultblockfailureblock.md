# addAssetsGroupAlbum(withName:resultBlock:failureBlock:)

**Framework**: Assets Library  
**Kind**: method

Adds a new assets group to the library.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func addAssetsGroupAlbum(withName name: String!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)
```

#### Discussion

The name of the new asset group is `name`, its type is [`ALAssetsGroupAlbum`](alassetsgroupalbum.md), and the [`isEditable`](alassetsgroup/iseditable.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

This method is asynchronous. When the assets group is added, the user may be asked to confirm the application’s access to the data; the method, though, returns immediately. You should perform whatever work you want with the group in `resultBlock`.

If the user denies access to the application, or if no application is allowed to access the data, or if the data is currently unavailable, the failure block is called.

## Parameters

- `name`: If   conflicts with another assets group with the same name, then the group is not created and   returns a   group.
- `resultBlock`: For a description of the block, see  .
- `failureBlock`: For a description of the block, see  .

## See Also

- [func group(for: URL!, resultBlock: ALAssetsLibraryGroupResultBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/group(for:resultblock:failureblock:).md)
  Returns an assets group in the result block for a URL previously retrieved from an `ALAssetsGroup` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/addassetsgroupalbum(withname:resultblock:failureblock:))*