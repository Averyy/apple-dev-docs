# EnrollmentSSODocument

**Framework**: Device Management  
**Kind**: dictionary

Enrollment SSO streamlines the MDM enrollment process, reduces sign-ins, and improves security.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 2.0+

## Declaration

```swift
object EnrollmentSSODocument
```

## Properties

- `AppIDs` ([string]): An array of App IDs that specify apps that Enrollment SSO developer mode can use. In Enrollment SSO documents delivered through the developer endpoint, this key must be present and contain at least one value. In Enrollment SSO documents delivered by the standard Enrollment SSO endpoint, this key must not be present.
- `AssociatedDomains` ([string]): An array of associated domains that the device uses with the Enrollment SSO extension.
- `AssociatedDomainsEnableDirectDownloads` (boolean): If `true,` allows the domain to directly verify site association, instead of at Apple’s servers. Use this verification only with domains that are inaccessible on the public Internet.
- `ConfigurationProfile` (data): The profile containing an [`ExtensibleSingleSignOn`](extensiblesinglesignon.md) payload that specifies the SSO extension in the downloaded app prior to enrollment. This profile may contain certificate payloads. One of `ConfigurationProfile` and `Declarations` must be present.
- `Declarations` ([data]): An array of base64-encoded JSON formatted Declarative Device Management declarations that specify the managed app and its configuration, including any certificates or identities. The set of declarations must include one `com.apple.configuration.app.managed` configuration, and one activation declaration that references the configuration. Include asset declarations if the app config requires them. The app configuration must include `AppStoreID` when developer mode is not being used, or it must include `BundleID` when developer mode is used. One of `ConfigurationProfile` and `Declarations` must be present. Available: iOS 18.4+ | iPadOS 18.4+ | visionOS 2.4+
- `iTunesStoreID` (integer): The iTunes Store ID of the app to download prior to enrollment, to support Enrollment SSO during enrollment. Using developer mode ignores this key.

## See Also

- [Discover Authentication Servers](get-.well-known-com.apple.remotemanagement.md)
  Get a list of available authentication servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enrollmentssodocument)*