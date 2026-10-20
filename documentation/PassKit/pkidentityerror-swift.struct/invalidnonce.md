# invalidNonce

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

An error that indicates the number is too large or unsuitable.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var invalidNonce: PKIdentityError.Code { get }
```

## See Also

### Constants
- [static var cancelled: PKIdentityError.Code](./cancelled.md)
  An error that indicates the user cancels the presented sheet.
- [static var invalidElement: PKIdentityError.Code](./invalidelement.md)
  An error that indicates an element the app requests isn’t valid.
- [static var notSupported: PKIdentityError.Code](./notsupported.md)
  An error that indicates the request originates from a device the framework doesn’t support.
- [static var networkUnavailable: PKIdentityError.Code](./networkunavailable.md)
  An error that indicates a network isn’t available.
- [static var noElementsRequested: PKIdentityError.Code](./noelementsrequested.md)
  An error that indicates the elements aren’t supported.
- [static var requestAlreadyInProgress: PKIdentityError.Code](./requestalreadyinprogress.md)
  An error that indicates a request is already in progress.
- [static var unknown: PKIdentityError.Code](./unknown.md)
  An error that indicates an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityerror-swift.struct/invalidnonce)*