# enumerateGroups(withTypes:using:failureBlock:)

**Framework**: Assets Library  
**Kind**: method

Invokes a given block passing as a parameter each of the asset groups that match the given asset group type.

## Declaration

```swift
func enumerateGroups(withTypes types: ALAssetsGroupType, using enumerationBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)
```

#### Discussion

The results are passed one by one to the caller by executing the enumeration block.

This method is asynchronous. When groups are enumerated, the user may be asked to confirm the application’s access to the data; the method, though, returns immediately. You should perform whatever work you want with the assets in `enumerationBlock`.

If the user denies access to the application, or if no application is allowed to access the data, the `failureBlock` is called.

##### Special Considerations

This method will fail with error [`ALAssetsLibraryAccessGloballyDeniedError`](alassetslibraryaccessgloballydeniederror.md) if the user has not enabled Location Services (in Settings > General).

## Parameters

- `types`: The types of asset group over which to enumerate. The value is a bitfield; you can OR together values from [`writeImageData(toSavedPhotosAlbum:metadata:completionBlock:)`](alassetslibrary/writeimagedata(tosavedphotosalbum:metadata:completionblock:).md).
- `enumerationBlock`: The block to invoke using each asset group in turn. When the enumeration is done, `enumerationBlock` is invoked with `group` set to `nil`. For a description of the block, see [`ALAssetsLibraryGroupsEnumerationResultsBlock`](alassetslibrarygroupsenumerationresultsblock.md).
- `failureBlock`: The block to invoke if the user denies access to the assets library. For a description of the block, see [`ALAssetsLibraryAccessFailureBlock`](alassetslibraryaccessfailureblock.md).

## See Also

- [func enumerateGroupsWithTypes(UInt32, usingBlock: ALAssetsLibraryGroupsEnumerationResultsBlock!, failureBlock: ALAssetsLibraryAccessFailureBlock!)](alassetslibrary/enumerategroupswithtypes(_:usingblock:failureblock:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/enumerategroups(withtypes:using:failureblock:))*