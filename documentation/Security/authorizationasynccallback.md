# AuthorizationAsyncCallback

**Framework**: Security  
**Kind**: typealias

A block used as a callback for the asynchronous version of copying authorization rights.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
typealias AuthorizationAsyncCallback = (OSStatus, UnsafeMutablePointer<AuthorizationRights>?) -> Void
```

#### Discussion

Use a block of this type as the callback parameter to the [`AuthorizationCopyRightsAsync(_:_:_:_:_:)`](authorizationcopyrightsasync(_:_:_:_:_:).md) function.

## Parameters

- `err`: A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md). This is equivalent to the return value from the [`AuthorizationCopyRights(_:_:_:_:_:)`](authorizationcopyrights(_:_:_:_:_:).md) function.
- `blockAuthorizedRights`: The authorized rights. This is equivalent to the authorizedRights parameter of the [`AuthorizationCopyRights(_:_:_:_:_:)`](authorizationcopyrights(_:_:_:_:_:).md) function. Free this object using the [`AuthorizationFreeItemSet(_:)`](authorizationfreeitemset(_:).md) function when you are done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationasynccallback)*