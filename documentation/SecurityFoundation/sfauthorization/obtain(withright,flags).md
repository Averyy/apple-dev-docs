# obtain(withRight:flags:)

**Framework**: Security Foundation  
**Kind**: method  
**Role**: Instance Method

Authorizes and preauthorizes one specific right.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func obtain(withRight rightName: AuthorizationString!, flags: AuthorizationFlags) throws
```

```objc
- (BOOL) obtainWithRight:(AuthorizationString) rightName flags:(AuthorizationFlags) flags error:(NSError **) error;
```

## Return value

[`true`](../../Swift/true.md) if operation completes successfully.

## Discussion

Use this method to authorize or preauthorize a single right.

> **Handling Errors in Swift**: In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and [About Imported Cocoa Error Parameters](../../Swift/about-imported-cocoa-error-parameters.md).

## Parameters

- `rightName`: The name of an authorization right.
- `flags`: A bit mask for specifying authorization options. See [`obtain(withRights:flags:environment:authorizedRights:)`](./obtain%28withrights,flags,environment,authorizedrights%29.md) for details about possible flag values.

## See Also

### Authorizing rights
- [func obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](./obtain%28withrights,flags,environment,authorizedrights%29.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [- permitWithRights:flags:environment:authorizedRights:](./permitwithrights_flags_environment_authorizedrights_.md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.
- [- permitWithRight:flags:](./permitwithright_flags_.md)
  Authorizes and preauthorizes one specific right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/obtain(withright:flags:))*