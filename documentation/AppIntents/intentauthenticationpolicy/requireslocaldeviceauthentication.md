# IntentAuthenticationPolicy.requiresLocalDeviceAuthentication

**Framework**: App Intents  
**Kind**: case

A policy that requires the person to unlock the device running the intent.

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
case requiresLocalDeviceAuthentication
```

#### Discussion

Use this policy if your app intent relies on data or services that are only available when the current device is unlocked. The system asks the person to unlock their device if it’s currently locked, even if the request originated from an already authenticated Apple Watch or remote device. For example, you might use this option if your app intent accesses data on disk that’s encrypted when the device is locked.

## See Also

- [IntentAuthenticationPolicy.alwaysAllowed](intentauthenticationpolicy/alwaysallowed.md)
  A policy that allows the app intent to run at any time, including when the device is locked.
- [IntentAuthenticationPolicy.requiresAuthentication](intentauthenticationpolicy/requiresauthentication.md)
  A policy that requires authentication before running the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy/requireslocaldeviceauthentication)*