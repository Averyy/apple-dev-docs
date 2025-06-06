# manageUsers(completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Presents a view controller to manage users of the home.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+

## Declaration

```swift
func manageUsers() async throws
```

#### Discussion

Only users that have administrator access to the home can call this method. Otherwise, the completion handler returns the error [`HMError.Code.insufficientPrivileges`](hmerror/code/insufficientprivileges.md).

## Parameters

- `completion`: The block executed after the request is processed.

## See Also

- [var currentUser: HMUser](hmhome/currentuser.md)
  The current HomeKit user.
- [class HMUser](hmuser.md)
  A person in the home who may have access to control accessories and services in the home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/manageusers(completionhandler:))*