# NSFileManagerUnmountDissentingProcessIdentifierErrorKey

**Framework**: Foundation  
**Kind**: var

The process identifier of the process that prevented a volume from unmounting.

**Availability**:
- macOS 10.11+

## Declaration

```swift
let NSFileManagerUnmountDissentingProcessIdentifierErrorKey: String
```

#### Discussion

If [`unmountVolume(at:options:completionHandler:)`](filemanager/unmountvolume(at:options:completionhandler:).md) fails, the error sent to its completion handler will contain a `userInfo` dictionary with this string as one of its keys. The value is the process identifier of the process that prevented the unmounting, as an [`NSNumber`](nsnumber.md).

## See Also

- [func unmountVolume(at: URL, options: FileManager.UnmountOptions, completionHandler: ((any Error)?) -> Void)](filemanager/unmountvolume(at:options:completionhandler:).md)
  Starts the process of unmounting the specified volume.
- [FileManager.UnmountOptions](filemanager/unmountoptions.md)
  Options that specify the behavior of an unmount operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerunmountdissentingprocessidentifiererrorkey)*