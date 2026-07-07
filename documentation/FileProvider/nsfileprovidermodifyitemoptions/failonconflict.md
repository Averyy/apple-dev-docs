# failOnConflict

**Framework**: File Provider  
**Kind**: property

An option to fail an upload in the event of a version conflict.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var failOnConflict: NSFileProviderModifyItemOptions { get }
```

#### Discussion

If you adopt this option, and an uploaded item’s base version doesn’t match the version on the server, fail and return [`localVersionConflictingWithServer`](nsfileprovidererror/localversionconflictingwithserver.md) (Swift) or [`NSFileProviderError.Code.localVersionConflictingWithServer`](nsfileprovidererror/code/localversionconflictingwithserver.md) (Objective-C) in your implementation of `modifyItem`.

To support the fail-on-conflict behavior in your file provider, indicate the support by adding the following key/value pair to the extension’s Info pane.

```None
<key>NSExtension</key>
<dict>
    <key>NSExtensionFileProviderSupportsFailingUploadOnConflict</key>
    <true/>
</dict>
```

## See Also

- [static var mayAlreadyExist: NSFileProviderModifyItemOptions](nsfileprovidermodifyitemoptions/mayalreadyexist.md)
  An option that indicates the changes may already exist in your remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermodifyitemoptions/failonconflict)*