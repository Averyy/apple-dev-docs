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

- `types`: The value is a bitfield; you can OR together values from  .
- `enumerationBlock`: For a description of the block, see  .
- `failureBlock`: For a description of the block, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/enumerategroups(withtypes:using:failureblock:))*