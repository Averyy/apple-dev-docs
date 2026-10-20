# PKIdentityError.Code.requestAlreadyInProgress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

An error that indicates a request is already in progress.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case requestAlreadyInProgress
```

```c
PKIdentityErrorRequestAlreadyInProgress
```

## Mentions

- [Requesting identity data from a Wallet pass](../../requesting-identity-data-from-a-wallet-pass.md)

## See Also

### Error codes
- [PKIdentityError.Code.cancelled](./cancelled.md)
  An error that indicates the user cancels the presented sheet.
- [PKIdentityError.Code.invalidElement](./invalidelement.md)
  An error that indicates an element the app requests isn’t valid.
- [PKIdentityError.Code.invalidNonce](./invalidnonce.md)
  An error that indicates the number is too large or unsuitable.
- [PKIdentityError.Code.notSupported](./notsupported.md)
  An error that indicates the request originates from a device the framework doesn’t support.
- [PKIdentityError.Code.networkUnavailable](./networkunavailable.md)
  An error that indicates a network isn’t available.
- [PKIdentityError.Code.noElementsRequested](./noelementsrequested.md)
  An error that indicates the elements aren’t supported.
- [PKIdentityError.Code.unknown](./unknown.md)
  An error that indicates an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityerror-swift.struct/code/requestalreadyinprogress)*