# CKErrorDomain

**Framework**: CloudKit  
**Kind**: var

The error domain for CloudKit errors.

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
let CKErrorDomain: String
```

## See Also

- [struct CKError](ckerror.md)
  A type that describes a CloudKit error.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
- [let CKErrorRetryAfterKey: String](ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKErrorUserDidResetEncryptedDataKey: String](ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerrordomain)*