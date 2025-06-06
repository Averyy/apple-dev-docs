# requestAuthorization(completionHandler:)

**Framework**: FamilyControls  
**Kind**: method

Requests authorization to provide parental controls for a child.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func requestAuthorization(completionHandler: @escaping (Result<Void, any Error>) -> Void)
```

## Parameters

- `completionHandler`: A closure the system calls after it completes the authorization request.

## See Also

- [func requestAuthorization(for: FamilyControlsMember) async throws](authorizationcenter/requestauthorization(for:).md)
  Requests authorization to provide parental controls for a child or individual.
- [func revokeAuthorization(completionHandler: (Result<Void, any Error>) -> Void)](authorizationcenter/revokeauthorization(completionhandler:).md)
  Revokes authorization to provide parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationcenter/requestauthorization(completionhandler:))*