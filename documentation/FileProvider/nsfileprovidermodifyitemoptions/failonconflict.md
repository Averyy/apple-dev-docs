# failOnConflict

**Framework**: File Provider  
**Kind**: property

If the base version of the item trying to be uploaded doesn’t match the version of the file on server, the call to modifyItem should fail with a NSFileProviderErrorLocalVersionConflictingWithServer error.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static var failOnConflict: NSFileProviderModifyItemOptions { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermodifyitemoptions/failonconflict)*