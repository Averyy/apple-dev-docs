# fileIconKey

**Framework**: Foundation  
**Kind**: property

A key with a corresponding value that must be an image, typically an icon to represent the file.

**Availability**:
- macOS 10.9+

## Declaration

```swift
static let fileIconKey: ProgressUserInfoKey
```

#### Discussion

If present, the Finder uses this corresponding value to show the icon of a file that a progress object is tracking.

## See Also

- [static let fileAnimationImageKey: ProgressUserInfoKey](progressuserinfokey/fileanimationimagekey.md)
  A key with a corresponding value that is an image, typically an icon to represent the file.
- [static let fileAnimationImageOriginalRectKey: ProgressUserInfoKey](progressuserinfokey/fileanimationimageoriginalrectkey.md)
  A key with a corresponding value that indicates the starting location of the image onscreen.
- [static let fileCompletedCountKey: ProgressUserInfoKey](progressuserinfokey/filecompletedcountkey.md)
  A key with a corresponding value that represents the number of completed files.
- [static let fileOperationKindKey: ProgressUserInfoKey](progressuserinfokey/fileoperationkindkey.md)
  A key with a corresponding value that indicates the kind of file operation a progress object represents.
- [static let fileTotalCountKey: ProgressUserInfoKey](progressuserinfokey/filetotalcountkey.md)
  A key with a corresponding value that represents the total number of files within a file operation.
- [static let fileURLKey: ProgressUserInfoKey](progressuserinfokey/fileurlkey.md)
  A key with a corresponding value that represents the file URL of a file operation for the progress object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressuserinfokey/fileiconkey)*