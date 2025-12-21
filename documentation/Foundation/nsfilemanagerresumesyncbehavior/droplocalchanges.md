# NSFileManagerResumeSyncBehavior.dropLocalChanges

**Framework**: Foundation  
**Kind**: case

Resumes synchronizing by overwriting any local changes with the remote version of the file.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case dropLocalChanges
```

#### Discussion

If a conflict occurs, the file manager stores the local changes as an alternate version. Only use this behavior if you provide a separate means of resolving and merging conflicts.

## See Also

- [NSFileManagerResumeSyncBehavior.preserveLocalChanges](nsfilemanagerresumesyncbehavior/preservelocalchanges.md)
  Resumes synchronizing by uploading the local version of the file.
- [NSFileManagerResumeSyncBehavior.afterUploadWithFailOnConflict](nsfilemanagerresumesyncbehavior/afteruploadwithfailonconflict.md)
  Resumes sync by first uploading the local version of the file, failing if the provider detects a conflict.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilemanagerresumesyncbehavior/droplocalchanges)*