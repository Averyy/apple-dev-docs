# fileAnimationImageOriginalRectKey

**Framework**: Foundation  
**Kind**: property

A key with a corresponding value that indicates the starting location of the image onscreen.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static let fileAnimationImageOriginalRectKey: ProgressUserInfoKey
```

#### Discussion

The associated value is an [`NSValue`](nsvalue.md) that contains an [`NSRect`](nsrect.md), in screen coordinates. This entry is optional, but if present, along with a value for [`fileAnimationImageKey`](progressuserinfokey/fileanimationimagekey.md), the Dock may show an animation. When the Dock has an item for the folder that contains the relevant file (such as the Downloads folder), the Dock uses this key to show an animation of the file flying into the Dock.

## See Also

- [static let fileAnimationImageKey: ProgressUserInfoKey](progressuserinfokey/fileanimationimagekey.md)
  A key with a corresponding value that is an image, typically an icon to represent the file.
- [static let fileCompletedCountKey: ProgressUserInfoKey](progressuserinfokey/filecompletedcountkey.md)
  A key with a corresponding value that represents the number of completed files.
- [static let fileIconKey: ProgressUserInfoKey](progressuserinfokey/fileiconkey.md)
  A key with a corresponding value that must be an image, typically an icon to represent the file.
- [static let fileOperationKindKey: ProgressUserInfoKey](progressuserinfokey/fileoperationkindkey.md)
  A key with a corresponding value that indicates the kind of file operation a progress object represents.
- [static let fileTotalCountKey: ProgressUserInfoKey](progressuserinfokey/filetotalcountkey.md)
  A key with a corresponding value that represents the total number of files within a file operation.
- [static let fileURLKey: ProgressUserInfoKey](progressuserinfokey/fileurlkey.md)
  A key with a corresponding value that represents the file URL of a file operation for the progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressuserinfokey/fileanimationimageoriginalrectkey)*