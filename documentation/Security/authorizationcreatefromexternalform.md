# AuthorizationCreateFromExternalForm(_:_:)

**Framework**: Security  
**Kind**: func

Internalizes the external representation of an authorization reference.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationCreateFromExternalForm(_ extForm: UnsafePointer<AuthorizationExternalForm>, _ authorization: UnsafeMutablePointer<AuthorizationRef?>) -> OSStatus
```

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

When passing an authorization reference between processes, use this function to internalize the external representation of the authorization reference you created using the function [`AuthorizationMakeExternalForm(_:_:)`](authorizationmakeexternalform(_:_:).md).

## Parameters

- `extForm`: A pointer to the external representation of the authorization reference you retrieve from the calling process.
- `authorization`: A pointer to an authorization reference. On return, this points to the local copy of the authorization reference. The Security Server allocates the authorization reference for you, so you do not need to call the function  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcreatefromexternalform(_:_:))*