# IntentAuthenticationPolicy.requiresAuthentication

**Framework**: App Intents  
**Kind**: case

A policy that requires authentication before running the app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
case requiresAuthentication
```

#### Discussion

Use this policy if you require some type of authentication before the system runs the app intent. If the app intent originates on one device, but runs on another device, only one of the devices needs to be unlocked. For example, if someone starts an app intent on their unlocked Apple Watch, the system doesn’t require additional authentication even if your app intent’s code runs on a locked iPhone. If both devices are locked, the system prompts the person to authenticate before running the app intent.

## See Also

- [IntentAuthenticationPolicy.alwaysAllowed](intentauthenticationpolicy/alwaysallowed.md)
  A policy that allows the app intent to run at any time, including when the device is locked.
- [IntentAuthenticationPolicy.requiresLocalDeviceAuthentication](intentauthenticationpolicy/requireslocaldeviceauthentication.md)
  A policy that requires the person to unlock the device running the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy/requiresauthentication)*