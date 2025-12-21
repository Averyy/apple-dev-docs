# Error constants

**Framework**: PassKit (Apple Pay and Wallet)

Error code constants for identity operations.

## Topics

### Constants
- [static var cancelled: PKIdentityError.Code](pkidentityerror-swift.struct/cancelled.md)
  An error that indicates the user cancels the presented sheet.
- [static var invalidElement: PKIdentityError.Code](pkidentityerror-swift.struct/invalidelement.md)
  An error that indicates an element the app requests isn’t valid.
- [static var invalidNonce: PKIdentityError.Code](pkidentityerror-swift.struct/invalidnonce.md)
  An error that indicates the number is too large or unsuitable.
- [static var notSupported: PKIdentityError.Code](pkidentityerror-swift.struct/notsupported.md)
  An error that indicates the request originates from a device the framework doesn’t support.
- [static var networkUnavailable: PKIdentityError.Code](pkidentityerror-swift.struct/networkunavailable.md)
  An error that indicates a network isn’t available.
- [static var noElementsRequested: PKIdentityError.Code](pkidentityerror-swift.struct/noelementsrequested.md)
  An error that indicates the elements aren’t supported.
- [static var requestAlreadyInProgress: PKIdentityError.Code](pkidentityerror-swift.struct/requestalreadyinprogress.md)
  An error that indicates a request is already in progress.
- [static var unknown: PKIdentityError.Code](pkidentityerror-swift.struct/unknown.md)
  An error that indicates an unknown error.

## See Also

- [PKIdentityError.Code](pkidentityerror-swift.struct/code.md)
  Error codes for identity operations.
- [var errorCode: Int](../Foundation/CustomNSError/errorCode-2opgi.md)
  The error code within the given domain.
- [var userInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkidentityerror/3931651-userinfo.md)
  The user information for the error.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo-1aas5.md)
  The default user-info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/error-constants)*