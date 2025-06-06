# noElementsRequested

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An error that indicates the elements aren’t supported.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var noElementsRequested: PKIdentityError.Code { get }
```

## See Also

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
- [static var requestAlreadyInProgress: PKIdentityError.Code](pkidentityerror-swift.struct/requestalreadyinprogress.md)
  An error that indicates a request is already in progress.
- [static var unknown: PKIdentityError.Code](pkidentityerror-swift.struct/unknown.md)
  An error that indicates an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityerror-swift.struct/noelementsrequested)*