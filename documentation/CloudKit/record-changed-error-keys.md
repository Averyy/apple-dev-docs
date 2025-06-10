# Record Changed Error Keys

**Framework**: CloudKit

Constants that represent conflicting records in a save operation.

#### Overview

If the version of a record on the server is newer than the version you try to save, the server returns a [`CKError.Code.serverRecordChanged`](ckerror/code/serverrecordchanged.md) error. The error’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary contains the different versions of the conflicting records. Use these keys to retrieve the records, and to perform any resolution logic necessary to resolve the conflict.

## Topics

### Record Changed Error Keys
- [let CKRecordChangedErrorAncestorRecordKey: String](ckrecordchangederrorancestorrecordkey.md)
  The key to retrieve the original version of the record.
- [let CKRecordChangedErrorClientRecordKey: String](ckrecordchangederrorclientrecordkey.md)
  The key to retrieve the local version of the record.
- [let CKRecordChangedErrorServerRecordKey: String](ckrecordchangederrorserverrecordkey.md)
  The key to retrieve the server’s version of the record.

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
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/record-changed-error-keys)*