# AuthorizationCopyRightsAsync(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Authorizes and preauthorizes rights asynchronously.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func AuthorizationCopyRightsAsync(_ authorization: AuthorizationRef, _ rights: UnsafePointer<AuthorizationRights>, _ environment: UnsafePointer<AuthorizationEnvironment>?, _ flags: AuthorizationFlags, _ callbackBlock: @escaping AuthorizationAsyncCallback)
```

#### Discussion

See the discussion for [`AuthorizationCopyRights(_:_:_:_:_:)`](authorizationcopyrights(_:_:_:_:_:).md). This function behaves similarly, except that it performs its operations asynchronously and calls back to you upon completion.

## Parameters

- `authorization`: An authorization reference referring to the authorization session.
- `rights`: A pointer to a set of authorization rights you create. Pass `nil` if the application requires no rights at this time.
- `environment`: Data used when authorizing or preauthorizing rights. Not used in OS X v10.2 and earlier. In macOS 10.3 and later, you can pass icon or prompt data to be used in the authentication dialog box. In macOS 10.4 and later, you can also pass a user name and password in order to authorize a user without displaying the authentication dialog box. Possible values for this parameter are listed in `Security.framework/Headers/AuthorizationTags.h`. The data passed in this parameter is not stored in the authorization reference; it is used only during authorization. If you are not passing any data in this parameter, pass the constant [`kAuthorizationEmptyEnvironment`](kauthorizationemptyenvironment.md).
- `flags`: A bit mask for specifying authorization options. Use one of the options sets defined for the flags parameter in the [`AuthorizationCopyRights(_:_:_:_:_:)`](authorizationcopyrights(_:_:_:_:_:).md) function.
- `callbackBlock`: A callback that you provide for the function to call when it finishes asynchronously. Use a function with the signature defined by [`AuthorizationAsyncCallback`](authorizationasynccallback.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcopyrightsasync(_:_:_:_:_:))*