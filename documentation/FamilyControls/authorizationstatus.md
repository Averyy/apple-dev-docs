# AuthorizationStatus

**Framework**: Family Controls  
**Kind**: enum  
**Role**: Enumeration

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
- [AuthorizationStatus.notDetermined](./authorizationstatus/notdetermined.md)
  The app hasn’t requested authorization.
- [AuthorizationStatus.denied](./authorizationstatus/denied.md)
  The person, parent, or guardian denied the request for authorization.
- [AuthorizationStatus.approved](./authorizationstatus/approved.md)
  The person, parent, or guardian approved the request for authorization.
- [AuthorizationStatus.approvedWithDataAccess](./authorizationstatus/approvedwithdataaccess.md)
  The person, parent, or guardian approved the request for authorization with access to non-tokenized family activity data.
### Debugging
- [var description: String](./authorizationstatus/description.md)
  A nonlocalized description of the authorization value, suitable for debugging.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Authorizations
- [class AuthorizationCenter](./authorizationcenter.md)
  The center for requesting authorization to provide parental controls.
- [Family Controls](../BundleResources/entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.
- [Requesting the Family Controls entitlement](./requesting-the-family-controls-entitlement.md)
  Register your app and its Screen Time API app extensions to use Family Controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationstatus)*