# com.apple.developer.on-demand-install-capable

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether a bundle represents an App Clip.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

Adding an App Clip target to your project as described in [`Creating an App Clip with Xcode`](https://developer.apple.com/documentation/AppClip/creating-an-app-clip-with-xcode) enables a capability called On Demand Install Capable for the App Clip target.

When you code-sign your full app, Xcode embeds the App Clip in the full app and applies the `com.apple.developer.on-demand-install-capable` entitlement. Because of this behavior, the App Clip’s `.entitlements` file doesn’t include this entitlement if you open the file in Xcode’s Project navigator.

To see the entitlement in the `.entitlements` file, first archive the full app, then export the App Clip for distribution as described in [`Distributing your App Clip`](https://developer.apple.com/documentation/AppClip/distributing-your-app-clip). Next, open the Terminal app and run `codesign -d --entitlements :- /path/to/ExampleApp.app/AppClips/ExampleAppClip.app`.

## See Also

- [Parent Application Identifiers Entitlement](entitlements/com.apple.developer.parent-application-identifiers.md)
  A list of parent application identifiers for an App Clip with exactly one entry.
- [com.apple.developer.associated-appclip-app-identifiers](entitlements/com.apple.developer.associated-appclip-app-identifiers.md)
  A list of App Clip identifiers for an app with exactly one entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.on-demand-install-capable)*