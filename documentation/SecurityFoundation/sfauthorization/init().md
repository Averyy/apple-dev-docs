# init()

**Framework**: Security Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an authorization object with default environment, flags, and rights.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init!()
```

```objc
- (id) init;
```

## See Also

### Allocating and initializing an authorization object
- [class func authorization() -> Any!](./authorization%28%29.md)
  Returns an authorization object initialized with a default environment, flags, and rights.
- [class func authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!](./authorization%28with,rights,environment%29.md)
  Returns an authorization object initialized with the specified flags, rights and environment.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](./init%28flags,rights,environment%29.md)
  Initializes an authorization object with the specified flags, rights, and environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/init())*