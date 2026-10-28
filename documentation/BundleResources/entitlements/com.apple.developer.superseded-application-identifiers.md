# App Replacement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

An entitlement that allows an app to offer the ability to migrate settings and data from and replace an older app with a specified app identifier.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+

## Details

- **Name**: `com.apple.developer.superseded-application-identifiers`
- **Type**: array of string 

## Discussion

This entitlement enables you to replace apps on iOS and iPadOS using a prioritized list of app identifiers associated with your developer account. On the first launch of an app that has adopted this entitlement and provided a list of one or more app identifiers associated with your developer account, the system enumerates the identifiers in the order presented in the list. For the first enumerated identifier that matches an app someone has already installed on the device, the system gives the person the option of replacing the app with a new app that inherits the older app’s data and settings. If the person agrees to the replacement, the system deletes the older app once the data and settings migration process completes.

The app replacement offer process is a first-run activity and runs only once.

> ❗ **Important**:  The original and the replacement app must be under the same developer membership, and they must have substantively the same primary purpose and functionality.

To request access to this capability, see [App Replacement Request](https://developer.apple.com/contact/request/app-replacement/).

### Adopt the entitlement

To adopt this entitlement, add it to your app’s capabilities by following these steps:

1. In the Xcode project navigator, select your app’s target, and then the Signing & Capabilities tab.
2. Add a new capability by clicking the + Capability button and then type “App Replacement” in the search field.
3. Double-click the App Replacement entry to add the entitlement to your app.
4. In the Xcode project navigator, double-click your app’s Entitlements file.
5. Select and edit the App Replacement dictionary entry and provide an array of app identifiers for past versions of the app in priority order, as shown in the following example. You can find app identifiers in the record for each app in your team’s account on the [Apple Developer portal](https://developer.apple.com).

```
<plist>
<dict>
    <key>com.apple.developer.superseded-application-identifiers</key>
    <array>
    <string>com.example.app-v3</string>
    <string>com.example.app-v2</string>
    <string>com.example.app-v1</string>
    </array>
</dict>
</plist>
```

You can test the app placement workflow using [TestFlight](https://testflight.apple.com).


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.superseded-application-identifiers)*