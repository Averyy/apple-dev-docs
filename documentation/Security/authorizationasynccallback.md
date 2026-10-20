# AuthorizationAsyncCallback

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(int, AuthorizationItemSet *) AuthorizationAsyncCallback;
```

#### Discussion

Use a block of this type as the callback parameter to the [`AuthorizationCopyRightsAsync(_:_:_:_:_:)`](./authorizationcopyrightsasync%28_,_,_,_,_%29.md) function.

## Parameters

- `err`: A result code. See [Authorization Services Result Codes](./authorization-services-result-codes.md). This is equivalent to the return value from the [`AuthorizationCopyRights(_:_:_:_:_:)`](./authorizationcopyrights%28_,_,_,_,_%29.md) function.
- `blockAuthorizedRights`: The authorized rights. This is equivalent to the authorizedRights parameter of the [`AuthorizationCopyRights(_:_:_:_:_:)`](./authorizationcopyrights%28_,_,_,_,_%29.md) function. Free this object using the [`AuthorizationFreeItemSet(_:)`](./authorizationfreeitemset%28_%29.md) function when you are done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationasynccallback)*