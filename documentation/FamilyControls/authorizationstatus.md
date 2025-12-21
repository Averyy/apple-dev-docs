# AuthorizationStatus

**Framework**: FamilyControls  
**Kind**: enum

The status of your app’s authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
enum AuthorizationStatus
```

## Topics

### Determining the status
- [AuthorizationStatus.notDetermined](authorizationstatus/notdetermined.md)
  The app hasn’t requested authorization.
- [AuthorizationStatus.denied](authorizationstatus/denied.md)
  The user, parent, or guardian denied the request for authorization.
- [AuthorizationStatus.approved](authorizationstatus/approved.md)
  The user, parent, or guardian approved the request for authorization.
### Debugging
- [var description: String](authorizationstatus/description.md)
  A nonlocalized description of the authorization value, suitable for debugging.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [class AuthorizationCenter](authorizationcenter.md)
  The center for requesting authorization to provide parental controls.
- [Family Controls](../BundleResources/Entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.
- [Requesting the Family Controls entitlement](requesting-the-family-controls-entitlement.md)
  Register your app and its Screen Time API app extensions to use Family Controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationstatus)*