# close()

**Framework**: GameSave  
**Kind**: method  
**Role**: Instance Method

Closes the directory, and resumes syncing the directory to the cloud.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func close()
```

```objc
- (void) close;
```

## See Also

### Finishing with a directory
- [func triggerPendingUpload(completionHandler: (Bool) -> Void)](./triggerpendingupload%28completionhandler%29.md)
  Triggers an upload of the directory for any changes that were pending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamesave/gssynceddirectory/close())*