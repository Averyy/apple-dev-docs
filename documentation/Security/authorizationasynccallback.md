# AuthorizationAsyncCallback

**Framework**: Security  
**Kind**: typealias

A block used as a callback for the asynchronous version of copying authorization rights.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.7+

## Declaration

```swift
typealias AuthorizationAsyncCallback = (OSStatus, UnsafeMutablePointer<AuthorizationRights>?) -> Void
```

#### Discussion

Use a block of this type as the callback parameter to the [`AuthorizationCopyRightsAsync(_:_:_:_:_:)`](authorizationcopyrightsasync(_:_:_:_:_:).md) function.

## Parameters

- `err`: A result code. See  . This is equivalent to the return value from the   function.
- `blockAuthorizedRights`: The authorized rights. This is equivalent to the authorizedRights parameter of the   function. Free this object using the   function when you are done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationasynccallback)*