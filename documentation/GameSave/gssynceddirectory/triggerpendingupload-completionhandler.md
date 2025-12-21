# triggerPendingUpload(completionHandler:)

**Framework**: GameSave  
**Kind**: method

Triggers an upload of the directory for any changes that were pending.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func triggerPendingUpload() async -> Bool
```

#### Discussion

Calls the completion block with `YES` if there were pending uploads; otherwise with `NO`.

## See Also

- [func close()](gssynceddirectory/close.md)
  Closes the directory, and resumes syncing the directory to the cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/triggerpendingupload(completionhandler:))*