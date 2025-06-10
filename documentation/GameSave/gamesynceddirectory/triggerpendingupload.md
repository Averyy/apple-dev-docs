# triggerPendingUpload()

**Framework**: GameSave  
**Kind**: method

Triggers an upload of the directory for any changes that were pending.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func triggerPendingUpload() async -> Bool
```

#### Return Value

`true` if were pending uploads; otherwise `false`.

## See Also

- [func close()](gamesynceddirectory/close.md)
  Closes the directory, and resumes syncing the directory to the cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesynceddirectory/triggerpendingupload())*