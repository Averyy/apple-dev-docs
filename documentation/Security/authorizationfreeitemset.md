# AuthorizationFreeItemSet(_:)

**Framework**: Security  
**Kind**: func

Frees the memory associated with a set of authorization items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationFreeItemSet(_ set: UnsafeMutablePointer<AuthorizationItemSet>) -> OSStatus
```

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

When your application no longer needs the authorization item sets created by the Security Server in the [`AuthorizationCopyRights(_:_:_:_:_:)`](authorizationcopyrights(_:_:_:_:_:).md) and [`AuthorizationCopyInfo(_:_:_:)`](authorizationcopyinfo(_:_:_:).md) functions, call this function to free it.

## Parameters

- `set`: A pointer to the authorization set to free.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationfreeitemset(_:))*