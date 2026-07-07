# isImmediateUploadRequestByPresentingApplication

**Framework**: File Provider  
**Kind**: property

An option to require the upload to complete before calling the completion handler.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var isImmediateUploadRequestByPresentingApplication: NSFileProviderModifyItemOptions { get }
```

#### Discussion

This option allows the calling application to know when the uploaded version of the file is on the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermodifyitemoptions/isimmediateuploadrequestbypresentingapplication)*