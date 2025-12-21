# mayAlreadyExist

**Framework**: File Provider  
**Kind**: property

An option that indicates the changes may already exist in your remote storage.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var mayAlreadyExist: NSFileProviderModifyItemOptions { get }
```

#### Discussion

This option applies when moving the item to a location where it may refer to an item that already exists. This situation may occur when merging two directories together.

## See Also

- [static var failOnConflict: NSFileProviderModifyItemOptions](nsfileprovidermodifyitemoptions/failonconflict.md)
  An option to fail an upload in the event of a version conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermodifyitemoptions/mayalreadyexist)*