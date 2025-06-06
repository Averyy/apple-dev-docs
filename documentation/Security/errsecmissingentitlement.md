# errSecMissingEntitlement

**Framework**: Security  
**Kind**: var

A required entitlement is missing.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var errSecMissingEntitlement: OSStatus { get }
```

## Mentions

- [Sharing access to keychain items among a collection of apps](sharing-access-to-keychain-items-among-a-collection-of-apps.md)

#### Overview

The [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) method returns this error when you specify an access group to which your app doesn’t belong:

```swift
let attributes = [kSecClass: kSecClassGenericPassword,
                  kSecAttrService: service,
                  kSecAttrAccount: username,
                  kSecAttrAccessGroup: "group",
                  kSecValueData: password] as [String: Any]
let addStatus = SecItemAdd(attributes as CFDictionary, nil)
```

To avoid the error, either use your app’s default access group by omitting the [`kSecAttrAccessGroup`](ksecattraccessgroup.md) key in the add attributes, or make sure that the value associated with the key matches one of your app’s access groups. These access groups come from your app’s [`Keychain Access Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/keychain-access-groups), its app identifier, and its [`App Groups Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.application-groups), in that order, as described in [`Sharing access to keychain items among a collection of apps`](sharing-access-to-keychain-items-among-a-collection-of-apps.md).

You can check the access group string by setting a breakpoint on the [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) call and using the debugger to print the query dictionary. Look for the `agrp` item:

```sh
(lldb) p attributes
([String : Any]) $R0 = 5 key/value pairs {
...
  [3] = {
    key = "agrp"
    value = "SKMME9E2Y8.com.example.AppOne"
  }
...
}
```

If after setting the access group key correctly you still receive the `errSecMissingEntitlement` error, check to make sure the entitlements in your built app match your expectations. Build your app for a hardware target—not the Simulator app—and use Xcode to locate the app bundle on disk:

![Screenshot of Xcode showing how to find the full path to a built app bundle.](https://docs-assets.developer.apple.com/published/3e2ed90d0f429cda500e6d525afe04af/media-3370373%402x.png)

Then get a list of the app’s entitlements. Run the codesign command-line utility shown in the following example, substituting the Xcode-provided path to your app, like the one highlighted in the preceding illustration.

```sh
$ codesign -d --entitlements :- [path]


<plist version="1.0">
<dict>
   <key>com.apple.developer.team-identifier</key>
   <string>SKMME9E2Y8</string>
   <key>application-identifier</key>
   <string>SKMME9E2Y8.com.example.AppOne</string>
   <key>keychain-access-groups</key>
   <array>
       <string>SKMME9E2Y8.com.example.SharedItems</string>
   </array>
   <key>com.apple.security.application-groups</key>
   <array>
       <string>group.com.example.AppSuite</string>
   </array>
</dict>
</plist>
```

Inspect the codesign output to determine the groups to which your app actually belongs. The following collectively define your app’s access groups:

- Any of the strings in the array associated with the `keychain-access-groups` key.
- The string corresponding to the `application-identifier` key (or the `com.apple.application-identifier` key in macOS).
- Any of the strings in the array associated with the `com.apple.security.application-groups` key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errsecmissingentitlement)*