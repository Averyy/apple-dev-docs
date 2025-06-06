# CKPartialErrorsByItemIDKey

**Framework**: CloudKit  
**Kind**: var

The key to retrieve partial errors.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let CKPartialErrorsByItemIDKey: String
```

#### Discussion

The value of this key is a dictionary that maps an item ID to an error. The type of each ID depends on where the error occurs. For example, if you receive a partial error when modifying a record, the ID is an instance of [`CKRecord.ID`](ckrecord/id.md) that corresponds to the record that CloudKit can’t modify.

## See Also

- [let CKErrorDomain: String](ckerrordomain.md)
  The error domain for CloudKit errors.
- [struct CKError](ckerror.md)
  A type that describes a CloudKit error.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
- [let CKErrorRetryAfterKey: String](ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKErrorUserDidResetEncryptedDataKey: String](ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckpartialerrorsbyitemidkey)*