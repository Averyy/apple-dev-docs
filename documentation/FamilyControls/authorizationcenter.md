# AuthorizationCenter

**Framework**: FamilyControls  
**Kind**: class

The center for requesting authorization to provide parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
class AuthorizationCenter
```

#### Overview

To authorize your app so that it can provide parental controls, access the shared `AuthorizationCenter` instance.

```swift
let center = AuthorizationCenter.shared
```

> ❗ **Important**: You must add the Family Controls capability to your app before you call the [`requestAuthorization(for:)`](authorizationcenter/requestauthorization(for:).md) or [`revokeAuthorization(completionHandler:)`](authorizationcenter/revokeauthorization(completionhandler:).md) methods. This capability adds the [`Family Controls`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.family-controls) entitlement to your app. In a compatible iPad or iPhone app running in visionOS, authorization attempts always fail. For more information, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

Next, to request authorization to provide parental controls, call [`requestAuthorization(completionHandler:)`](authorizationcenter/requestauthorization(completionhandler:).md)

```swift
center.requestAuthorization { result in
    switch result {
    case .success():
        // The request succeeded.
    case .failure(let error):
        // Handle the error here.
    }
}
```

or [`requestAuthorization(for:)`](authorizationcenter/requestauthorization(for:).md).

```swift
do {
    try await center.requestAuthorization(for: FamilyControlsMember.individual)
} catch {
    // Handle the error here.
}
```

Always request authorization when your app first launches. If the user’s parent or guardian hasn’t previously authorized your app, the system displays an alert. If the parent or guardian chooses to continue, it displays an authentication sheet. When a parent or guardian either approves or cancels the request, the system sends the result back to the `requestAuthorization(completionHandler:)` method’s completion handler.

If you’re authenticating an `individual` who hasn’t previously authorized your app, the system displays an alert. If the `individual` chooses to continue, the device asks to authorize that `individual` using Face ID or Touch ID.

After your app has been authorized, additional calls to `requestAuthorization(for:)` don’t display the authentication sheet or ask to authorize that individual using Face ID or Touch ID. Instead, the system sets the authorization status.

To observe changes to the authorization status, use the [`authorizationStatus`](authorizationcenter/authorizationstatus.md) property.

The status may change due to external events, such as a child graduating to an adult account, or a parent or guardian changing the status in Settings. You can also revoke authorization by calling [`revokeAuthorization(completionHandler:)`](authorizationcenter/revokeauthorization(completionhandler:).md)

## Topics

### Accessing the shared center
- [static let shared: AuthorizationCenter](authorizationcenter/shared.md)
  The shared center for requesting and revoking authorization.
### Requesting and revoking authorization
- [func requestAuthorization(for: FamilyControlsMember) async throws](authorizationcenter/requestauthorization(for:).md)
  Requests authorization to provide parental controls for a child or individual.
- [func revokeAuthorization(completionHandler: (Result<Void, any Error>) -> Void)](authorizationcenter/revokeauthorization(completionhandler:).md)
  Revokes authorization to provide parental controls.
### Tracking authorization changes
- [var authorizationStatus: AuthorizationStatus](authorizationcenter/authorizationstatus.md)
  The status of your app’s authorization to provide parental controls.
- [var $authorizationStatus: Published<AuthorizationStatus>.Publisher](authorizationcenter/$authorizationstatus.md)
  A publisher for the authorization status property.
### Deprecated APIs
- [func requestAuthorization(completionHandler: (Result<Void, any Error>) -> Void)](authorizationcenter/requestauthorization(completionhandler:).md)
  Requests authorization to provide parental controls for a child.

## Relationships

### Conforms To
- [ObservableObject](../Combine/ObservableObject.md)

## See Also

- [enum AuthorizationStatus](authorizationstatus.md)
  The status of your app’s authorization to provide parental controls.
- [Family Controls](../BundleResources/Entitlements/com.apple.developer.family-controls.md)
  A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.
- [Requesting the Family Controls entitlement](requesting-the-family-controls-entitlement.md)
  Register your app and its Screen Time API app extensions to use Family Controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationcenter)*