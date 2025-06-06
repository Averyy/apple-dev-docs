# iCloud Services Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The iCloud services used by the app.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

#### Discussion

To add this entitlement to your app, enable the iCloud capability and the iCloud Documents or CloudKit service in Xcode.

The value `CloudKit-Anonymous` is only available to App Clips, but App Clips can’t use the values `CloudDocuments` or `CloudKit`. For more information on using CloudKit in your App Clip, see [`Sharing data between your App Clip and your full app`](https://developer.apple.com/documentation/AppClip/sharing-data-between-your-app-clip-and-your-full-app).

## See Also

- [com.apple.developer.icloud-container-development-container-identifiers](entitlements/com.apple.developer.icloud-container-development-container-identifiers.md)
  The container identifiers for the iCloud development environment.
- [com.apple.developer.icloud-container-environment](entitlements/com.apple.developer.icloud-container-environment.md)
  The development or production environment to use for the iCloud containers.
- [iCloud Container Identifiers Entitlement](entitlements/com.apple.developer.icloud-container-identifiers.md)
  The container identifiers for the iCloud production environment.
- [iCloud Key-Value Store Entitlement](entitlements/com.apple.developer.ubiquity-kvstore-identifier.md)
  The container identifier to use for iCloud key-value storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.icloud-services)*