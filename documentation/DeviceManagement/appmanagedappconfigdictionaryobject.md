# AppManagedAppConfigDictionaryObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary of app config data and credentials.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AppManagedAppConfigDictionaryObject
```

## Mentions

- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)

## Topics

### Objects
- [object AppManagedCredentialConfigObject](appmanagedcredentialconfigobject.md)
  A dictionary of values associated with a credential config.

## Properties

- `Certificates` ([AppManagedCredentialConfigObject]): Provides certificates to the managed app or extension. Each element in the array contains a certificate asset reference and an associated identifier which the app or extension uses to look up the certificate.
- `DataAssetReference` (string): Specifies the identifier of an asset declaration containing a reference to the app or extension config data. The corresponding asset needs to be of type `com.apple.asset.data`. The referenced data needs to be a property list file, and the asset’s “ContentType” value set to match the data type.
- `Identities` ([AppManagedCredentialConfigObject]): Provides identities to the managed app or extension. Each element in the array contains an identity asset reference and an associated identifier which the app or extension uses to look up the identity.
- `Passwords` ([AppManagedCredentialConfigObject]): Provides passwords to the managed app or extension. Each element in the array contains a password asset reference and an associated identifier which the app or extension uses to look up the password.

## See Also

- [object AppManagedAttributesObject](appmanagedattributesobject.md)
  A dictionary of values associated with an app.
- [object AppManagedExtensionConfigsObject](appmanagedextensionconfigsobject.md)
  A dictionary of values associated with an extension config.
- [object AppManagedInstallBehaviorObject](appmanagedinstallbehaviorobject.md)
  A dictionary that describes how and when to install an app.
- [object AppManagedUpdateBehaviorObject](appmanagedupdatebehaviorobject.md)
  Specifies the update behavior of the apps installed from the App Store. Apps in packages are not automatically updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appmanagedappconfigdictionaryobject)*