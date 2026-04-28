# AppManagedCredentialConfigObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of values associated with a credential config.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AppManagedCredentialConfigObject
```

## Mentions

- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)

## Properties

- `AssetReference` (string) *(required)*: Specifies the identifier of an asset declaration containing a username and password. The [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework makes the password available to the app or extension. The [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework ignores the username.
- `Identifier` (string) *(required)*: The app or extension uses this identifier to fetch the corresponding password using the [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp) framework. App developers define the values for these identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanagedcredentialconfigobject)*