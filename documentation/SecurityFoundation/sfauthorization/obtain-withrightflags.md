# obtain(withRight:flags:)

**Framework**: Securityfoundation  
**Kind**: method

Authorizes and preauthorizes one specific right.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func obtain(withRight rightName: AuthorizationString!, flags: AuthorizationFlags) throws
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if operation completes successfully.

#### Discussion

Use this method to authorize or preauthorize a single right.

> **Note**: In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and [`About Imported Cocoa Error Parameters`](https://developer.apple.com/documentation/Swift/about-imported-cocoa-error-parameters).

## Parameters

- `rightName`: The name of an authorization right.
- `flags`: A bit mask for specifying authorization options. See   for details about possible flag values.

## See Also

- [func obtain(withRights: UnsafePointer<AuthorizationRights>!, flags: AuthorizationFlags, environment: UnsafePointer<AuthorizationEnvironment>!, authorizedRights: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationRights>?>!) throws](sfauthorization/obtain(withrights:flags:environment:authorizedrights:).md)
  Authorizes and preauthorizes rights to access a privileged operation and returns the granted rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityfoundation/sfauthorization/obtain(withright:flags:))*