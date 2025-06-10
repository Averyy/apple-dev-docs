# Parent Application Identifiers Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A list of parent application identifiers for an App Clip with exactly one entry.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

The Parent Application Identifiers entitlement establishes a secure association between an App Clip and its corresponding app. Add it only to an App Clip target.

> **Note**:  When you add an App Clip target to your project as described in [`Creating an App Clip with Xcode`](https://developer.apple.com/documentation/AppClip/creating-an-app-clip-with-xcode), Xcode creates this entitlement and adds the correct value.

Because an App Clip is always associated with exactly one app, ensure the parent application entitlement has exactly one entry, the corresponding app’s application identifier.

Ensure that the application identifier for the App Clip uses the full app’s application identifier as its prefix, followed by a string. For example, if your app’s application identifier is `$(AppIdentifierPrefix)com.example.MyApp`, the App Clip’s application identifier may be `$(AppIdentifierPrefix)com.example.MyApp.Clip`.

## See Also

- [com.apple.developer.associated-appclip-app-identifiers](entitlements/com.apple.developer.associated-appclip-app-identifiers.md)
  A list of App Clip identifiers for an app with exactly one entry.
- [com.apple.developer.on-demand-install-capable](entitlements/com.apple.developer.on-demand-install-capable.md)
  A Boolean value that indicates whether a bundle represents an App Clip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.parent-application-identifiers)*