# unmountVolume(at:options:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Starts the process of unmounting the specified volume.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func unmountVolume(at url: URL, options mask: FileManager.UnmountOptions = []) async throws
```

#### Discussion

If the volume is encrypted, it is relocked after being unmounted.

## Parameters

- `url`: A file URL specifying the volume to be unmounted.
- `mask`: A bitmask of   that you can use to customize the unmount operation’s behavior.
- `completionHandler`: A block executed when the unmount operation completes. The block receives an error parameter which is   if unmounting was successful. Otherwise, it indicates why unmounting failed.

## See Also

- [FileManager.UnmountOptions](filemanager/unmountoptions.md)
  Options that specify the behavior of an unmount operation.
- [let NSFileManagerUnmountDissentingProcessIdentifierErrorKey: String](nsfilemanagerunmountdissentingprocessidentifiererrorkey.md)
  The process identifier of the process that prevented a volume from unmounting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/unmountvolume(at:options:completionhandler:))*