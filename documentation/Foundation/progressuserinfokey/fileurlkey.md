# fileURLKey

**Framework**: Foundation  
**Kind**: property

A key with a corresponding value that represents the file URL of a file operation for the progress object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let fileURLKey: ProgressUserInfoKey
```

#### Discussion

If present, [`Progress`](progress.md) presents additional information in its localized description.

## See Also

- [static let fileAnimationImageKey: ProgressUserInfoKey](progressuserinfokey/fileanimationimagekey.md)
  A key with a corresponding value that is an image, typically an icon to represent the file.
- [static let fileAnimationImageOriginalRectKey: ProgressUserInfoKey](progressuserinfokey/fileanimationimageoriginalrectkey.md)
  A key with a corresponding value that indicates the starting location of the image onscreen.
- [static let fileCompletedCountKey: ProgressUserInfoKey](progressuserinfokey/filecompletedcountkey.md)
  A key with a corresponding value that represents the number of completed files.
- [static let fileIconKey: ProgressUserInfoKey](progressuserinfokey/fileiconkey.md)
  A key with a corresponding value that must be an image, typically an icon to represent the file.
- [static let fileOperationKindKey: ProgressUserInfoKey](progressuserinfokey/fileoperationkindkey.md)
  A key with a corresponding value that indicates the kind of file operation a progress object represents.
- [static let fileTotalCountKey: ProgressUserInfoKey](progressuserinfokey/filetotalcountkey.md)
  A key with a corresponding value that represents the total number of files within a file operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressuserinfokey/fileurlkey)*