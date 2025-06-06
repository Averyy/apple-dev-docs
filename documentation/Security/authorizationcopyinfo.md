# AuthorizationCopyInfo(_:_:_:)

**Framework**: Security  
**Kind**: func

Retrieves supporting data such as the user name and other information gathered during evaluation of authorization.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationCopyInfo(_ authorization: AuthorizationRef, _ tag: AuthorizationString?, _ info: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>?>) -> OSStatus
```

## Mentions

- [Extending authorization services with plug-ins](extending-authorization-services-with-plug-ins.md)

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

An authorization plug-in can store the results of an authentication operation by calling the [`SetContextValue`](authorizationcallbacks/setcontextvalue.md) function. You can use the [`AuthorizationCopyInfo(_:_:_:)`](authorizationcopyinfo(_:_:_:).md) function to retrieve this information.

## Parameters

- `authorization`: An authorization reference referring to the authorization session.
- `tag`: An   specifying the type of data the Security Server should return. Pass   to retrieve all available information.
- `info`: A pointer to an authorization set the Security Server creates. On return, this set contains side-band authorization data. When this set is no longer needed, free the memory associated with it by calling the function  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcopyinfo(_:_:_:))*