# com.apple.developer.associated-appclip-app-identifiers

**Framework**: Bundleresources  
**Kind**: typealias

A list of App Clip identifiers for an app with exactly one entry.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

#### Discussion

The `com.apple.developer.associated-appclip-app-identifiers` entitlement provides an app with the bundle ID of its associated App Clip. Together with the [`Parent Application Identifiers Entitlement`](entitlements/com.apple.developer.parent-application-identifiers.md), the Associated App Clip Identifiers entitlement establishes an association between your App Clip and your app that the system uses to enable data sharing between them. For additional information on sharing data between your App Clip and your full app, see [`Sharing data between your App Clip and your full app`](https://developer.apple.com/documentation/AppClip/sharing-data-between-your-app-clip-and-your-full-app).

> **Note**:  Xcode adds this entitlement when you archive an app that includes an App Clip.

## See Also

- [Parent Application Identifiers Entitlement](entitlements/com.apple.developer.parent-application-identifiers.md)
  A list of parent application identifiers for an App Clip with exactly one entry.
- [com.apple.developer.on-demand-install-capable](entitlements/com.apple.developer.on-demand-install-capable.md)
  A Boolean value that indicates whether a bundle represents an App Clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.associated-appclip-app-identifiers)*