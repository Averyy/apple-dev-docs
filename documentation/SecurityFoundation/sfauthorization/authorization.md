# authorization()

**Framework**: Security Foundation  
**Kind**: method

Returns an authorization object initialized with a default environment, flags, and rights.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func authorization() -> Any!
```

#### Return Value

The authorization object.

## See Also

- [class func authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!](sfauthorization/authorization(with:rights:environment:).md)
  Returns an authorization object initialized with the specified flags, rights and environment.
- [init!()](sfauthorization/init.md)
  Initializes an authorization object with default environment, flags, and rights.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](sfauthorization/init(flags:rights:environment:).md)
  Initializes an authorization object with the specified flags, rights, and environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/authorization())*