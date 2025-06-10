# IntentAuthenticationPolicy.requiresAuthentication

**Framework**: App Intents  
**Kind**: case

A policy that requires the user to authenticate.

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

If the device is in a locked state and the request doesn’t originate on an authenticated remote device; for example a connected Apple Watch; the system prompts a person to unlock the device before it runs the app intent.

## See Also

- [IntentAuthenticationPolicy.alwaysAllowed](intentauthenticationpolicy/alwaysallowed.md)
  A policy that allows the app intent to always run, even on a locked device.
- [IntentAuthenticationPolicy.requiresLocalDeviceAuthentication](intentauthenticationpolicy/requireslocaldeviceauthentication.md)
  A policy that requires the user to authenticate on the local device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy/requiresauthentication)*