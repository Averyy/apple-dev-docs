# revokeAuthorization(completionHandler:)

**Framework**: Familycontrols  
**Kind**: method

Revokes authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func revokeAuthorization(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

#### Discussion

If your app’s authentication status is [`AuthorizationStatus.approved`](authorizationstatus/approved.md) this method revokes authentication.

> **Note**: This method has no effect if your app’s current authentication status is [`AuthorizationStatus.denied`](authorizationstatus/denied.md).

The completion handler’s [`Result`](https://developer.apple.com/documentation/Swift/Result) parameter indicates whether the request completed successfully. It doesn’t indicate your app’s authorization state.

After you revoke authorization, your app no longer provides parental controls, and the system no longer enforces restrictions, such as preventing the user from deleting your app.

## Parameters

- `completionHandler`: A closure the system calls after   it completes the authorization request.   The system passes the following parameters:

## See Also

- [func requestAuthorization(for: FamilyControlsMember) async throws](authorizationcenter/requestauthorization(for:).md)
  Requests authorization to provide parental controls for a child or individual.
- [func requestAuthorization(completionHandler: (Result<Void, any Error>) -> Void)](authorizationcenter/requestauthorization(completionhandler:).md)
  Requests authorization to provide parental controls for a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationcenter/revokeauthorization(completionhandler:))*