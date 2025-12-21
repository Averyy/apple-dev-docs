# IntentAuthenticationPolicy

**Framework**: App Intents  
**Kind**: enum

An enumeration that describes the authentication policy to use when running an app intent.

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
enum IntentAuthenticationPolicy
```

## Topics

### Authentication policies
- [IntentAuthenticationPolicy.alwaysAllowed](intentauthenticationpolicy/alwaysallowed.md)
  A policy that allows the app intent to always run, even on a locked device.
- [IntentAuthenticationPolicy.requiresAuthentication](intentauthenticationpolicy/requiresauthentication.md)
  A policy that requires the user to authenticate.
- [IntentAuthenticationPolicy.requiresLocalDeviceAuthentication](intentauthenticationpolicy/requireslocaldeviceauthentication.md)
  A policy that requires the user to authenticate on the local device.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var authenticationPolicy: IntentAuthenticationPolicy](appintent/authenticationpolicy.md)
  A property that defines the authentication policy that indicates whether this app intent requires the device to be unlocked or otherwise authenticated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentauthenticationpolicy)*