# CKErrorRetryAfterKey

**Framework**: CloudKit  
**Kind**: var

The key to retrieve the number of seconds to wait before you retry a request.

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
let CKErrorRetryAfterKey: String
```

#### Discussion

An [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) that contains the number of seconds until you can retry a request. CloudKit adds this key to the error’s [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary when the error code is [`CKError.Code.serviceUnavailable`](ckerror/code/serviceunavailable.md) or [`CKError.Code.requestRateLimited`](ckerror/code/requestratelimited.md).

## See Also

- [let CKErrorDomain: String](ckerrordomain.md)
  The error domain for CloudKit errors.
- [struct CKError](ckerror.md)
  A type that describes a CloudKit error.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
- [let CKErrorUserDidResetEncryptedDataKey: String](ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerrorretryafterkey)*