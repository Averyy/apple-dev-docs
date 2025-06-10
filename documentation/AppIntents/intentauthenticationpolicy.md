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
### Operators
- [static func == (IntentAuthenticationPolicy, IntentAuthenticationPolicy) -> Bool](intentauthenticationpolicy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](intentauthenticationpolicy/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentauthenticationpolicy/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](intentauthenticationpolicy/equatable-implementations.md)

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