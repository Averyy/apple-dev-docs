# authorization(with:rights:environment:)

**Framework**: Security Foundation  
**Kind**: method

Returns an authorization object initialized with the specified flags, rights and environment.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func authorization(with flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!) -> Any!
```

#### Return Value

The authorization object.

#### Discussion

Normally, such initialization is not required, as you pass in flags, rights, and environmental data when you request authorization.

## Parameters

- `flags`: A bit mask for specifying authorization options. Use the following option sets:
- `rights`: A pointer to a set of authorization rights you create. Pass   if the application requires no rights at this time.
- `environment`: Data used when authorizing or preauthorizing rights. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. Possible values for this parameter are listed in  . The data passed in this parameter is not stored in the authorization reference; it is used only during authorization. If you are not passing any data in this parameter, pass the constant  .

## See Also

- [class func authorization() -> Any!](sfauthorization/authorization.md)
  Returns an authorization object initialized with a default environment, flags, and rights.
- [init!()](sfauthorization/init.md)
  Initializes an authorization object with default environment, flags, and rights.
- [init!(flags: AuthorizationFlags, rights: UnsafePointer<AuthorizationRights>!, environment: UnsafePointer<AuthorizationEnvironment>!)](sfauthorization/init(flags:rights:environment:).md)
  Initializes an authorization object with the specified flags, rights, and environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/authorization(with:rights:environment:))*