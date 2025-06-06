# authorizationStatus

**Framework**: HomeKit  
**Kind**: property

The current state of the app’s access to home data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var authorizationStatus: HMHomeManagerAuthorizationStatus { get }
```

## Mentions

- [Enabling HomeKit in your app](enabling-homekit-in-your-app.md)

#### Discussion

The first time your app uses the HomeKit framework—typically, when you create a [`HMHomeManager`](hmhomemanager.md) instance—the system automatically prompts the user for permission to access home data. You don’t make an explicit request for access, but you can modify the behavior of your app based on the current authorization status. For example, if your app lacks access to home data, you might omit certain features from your UI.

The [`authorizationStatus`](hmhomemanager/authorizationstatus.md) property contains a bit field that indicates the current authorization status. Your app has home data authorization only when the [`authorized`](hmhomemanagerauthorizationstatus/authorized.md) bit is present:

```swift
if myHomeManager.authorizationStatus.contains(.authorized) {
    // The app is authorized to access home data.
}
```

Users can revoke permission at any time in the Settings app, so your app should always be prepared to handle errors caused by lack of access.

For more information about gaining authorization to access home data, see [`Enabling HomeKit in your app`](enabling-homekit-in-your-app.md).

## See Also

- [struct HMHomeManagerAuthorizationStatus](hmhomemanagerauthorizationstatus.md)
  The possible home-access states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanager/authorizationstatus)*