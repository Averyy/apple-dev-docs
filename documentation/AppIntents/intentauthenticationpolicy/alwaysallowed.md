# IntentAuthenticationPolicy.alwaysAllowed

**Framework**: App Intents  
**Kind**: case

A policy that allows the app intent to run at any time, including when the device is locked.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
case alwaysAllowed
```

## See Also

- [IntentAuthenticationPolicy.requiresAuthentication](intentauthenticationpolicy/requiresauthentication.md)
  A policy that requires authentication before running the app intent.
- [IntentAuthenticationPolicy.requiresLocalDeviceAuthentication](intentauthenticationpolicy/requireslocaldeviceauthentication.md)
  A policy that requires the person to unlock the device running the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy/alwaysallowed)*