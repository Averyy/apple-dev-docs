# NSFileManagerResumeSyncBehavior.preserveLocalChanges

**Framework**: Foundation  
**Kind**: case

Resumes synchronizing by uploading the local version of the file.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case preserveLocalChanges
```

#### Discussion

If the server has a newer version, the server may create a conflict copy of the file, or may automatically pick the winner of the conflict. Apps can choose to implement conflict handling themselves by passing `NSFileManagerResumeSyncBehaviorAfterUploadWithFailOnConflict`.

## See Also

- [NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict](nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict.md)
  Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.
- [NSFileManagerResumeSyncBehavior.dropLocalChanges](nsfilemanagerresumesyncbehavior/droplocalchanges.md)
  Resumes synchronizing by overwriting any local changes with the remote version of the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/preservelocalchanges)*