# CKErrorUserDidResetEncryptedDataKey

**Framework**: CloudKit  
**Kind**: var

The key that determines whether CloudKit deletes a record zone because of a user action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let CKErrorUserDidResetEncryptedDataKey: String
```

## Mentions

- [Encrypting User Data](encrypting-user-data.md)

#### Discussion

An [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that represents a Boolean value you use to determine whether a user action causes CloudKit to delete a record zone. CloudKit adds this key to the error’s `userInfo` dictionary when the error code is [`CKError.Code.zoneNotFound`](ckerror/code/zonenotfound.md).

## See Also

- [let CKErrorDomain: String](ckerrordomain.md)
  The error domain for CloudKit errors.
- [struct CKError](ckerror.md)
  A type that describes a CloudKit error.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
- [let CKErrorRetryAfterKey: String](ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerroruserdidresetencrypteddatakey)*