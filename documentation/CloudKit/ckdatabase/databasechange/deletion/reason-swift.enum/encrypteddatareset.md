# CKDatabase.DatabaseChange.Deletion.Reason.encryptedDataReset

**Framework**: CloudKit  
**Kind**: case

The user chose to reset all encrypted data for their account.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
case encryptedDataReset
```

#### Discussion

This is an indication that the user needed to reset encrypted data during account recovery, and is still interested in locally-cached data.

To minimize data loss, consider re-uploading locally-cached data to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/databasechange/deletion/reason-swift.enum/encrypteddatareset)*