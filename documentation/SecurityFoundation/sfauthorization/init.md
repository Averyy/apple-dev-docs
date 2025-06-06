# init()

**Framework**: Security Foundation  
**Kind**: init

Initializes an authorization object with default environment, flags, and rights.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init!()
```

## See Also

- [class func authorization() -> Any!](sfauthorization/authorization.md)
  Returns an authorization object initialized with a default environment, flags, and rights.
- [class func authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!](sfauthorization/authorization(with:rights:environment:).md)
  Returns an authorization object initialized with the specified flags, rights and environment.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](sfauthorization/init(flags:rights:environment:).md)
  Initializes an authorization object with the specified flags, rights, and environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/init())*