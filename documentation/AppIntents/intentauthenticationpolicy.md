# IntentAuthenticationPolicy

**Framework**: App Intents  
**Kind**: enum

The authentication policies you can apply to an app intent when it runs.

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
enum IntentAuthenticationPolicy
```

## Topics

### Authentication policies
- [IntentAuthenticationPolicy.alwaysAllowed](intentauthenticationpolicy/alwaysallowed.md)
  A policy that allows the app intent to run at any time, including when the device is locked.
- [IntentAuthenticationPolicy.requiresAuthentication](intentauthenticationpolicy/requiresauthentication.md)
  A policy that requires authentication before running the app intent.
- [IntentAuthenticationPolicy.requiresLocalDeviceAuthentication](intentauthenticationpolicy/requireslocaldeviceauthentication.md)
  A policy that requires the person to unlock the device running the intent.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [static var authenticationPolicy: IntentAuthenticationPolicy](appintent/authenticationpolicy.md)
  The authentication policy to enforce when running the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy)*