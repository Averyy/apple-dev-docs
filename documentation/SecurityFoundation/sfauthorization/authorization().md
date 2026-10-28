# authorization()

**Framework**: Security Foundation  
**Kind**: method  
**Role**: Type Method

Returns an authorization object initialized with a default environment, flags, and rights.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func authorization() -> Any!
```

```objc
+ (id) authorization;
```

## Return value

The authorization object.

## See Also

### Allocating and initializing an authorization object
- [class func authorization(with: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!](./authorization%28with,rights,environment%29.md)
  Returns an authorization object initialized with the specified flags, rights and environment.
- [init!()](./init%28%29.md)
  Initializes an authorization object with default environment, flags, and rights.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](./init%28flags,rights,environment%29.md)
  Initializes an authorization object with the specified flags, rights, and environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/authorization())*