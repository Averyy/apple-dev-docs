# triggerPendingUpload()

**Framework**: GameSave  
**Kind**: method  
**Role**: Instance Method

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

#### Return Value

`true` if there were pending uploads; otherwise `false`.

## See Also

### Finishing with a directory
- [func close()](./close%28%29.md)
  Closes the directory, and resumes syncing the directory to the cloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gamesavesynceddirectory/triggerpendingupload())*