# shouldStorePreferencesForCurrentUser

**Framework**: TV Services  
**Kind**: property

A Boolean value that indicates whether your app needs to retain a selected profile.

**Availability**:
- tvOS 16.0+

## Declaration

```swift
var shouldStorePreferencesForCurrentUser: Bool { get }
```

#### Discussion

> ❗ **Important**:  To create a [`TVUserManager`](tvusermanager.md) object, add the [`User Management Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.user-management) to your app or app extension, and select the Runs as Current User, Only When User-Independent Keychain is Available option.

 To create a [`TVUserManager`](tvusermanager.md) object, add the [`User Management Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.user-management) to your app or app extension, and select the Runs as Current User, Only When User-Independent Keychain is Available option.

Some apps rely on profiles to maintain separate information for each person who uses a shared device, such as a video content app that retains which shows they watch. To avoid interrupting people with a profile picker each time they launch your app, you can save the current user’s selection on a shared device. After someone selects a profile, use [`shouldStorePreferencesForCurrentUser`](tvusermanager/shouldstorepreferencesforcurrentuser.md) to determine whether to retain the profile selection or to prompt each time your app launches. This property might be [`false`](https://developer.apple.com/documentation/swift/false) if people share a device, but don’t configure multiple users on that device.

If the property’s value is [`false`](https://developer.apple.com/documentation/swift/false), display the profile picker to determine which profile to use for the current session, but don’t save the selected profile. If the value is [`true`](https://developer.apple.com/documentation/swift/true), and there isn’t a saved profile in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults), display the profile picker and save the selected profile for future use. If the value is [`true`](https://developer.apple.com/documentation/swift/true) and there’s already a saved profile, skip the prompt and use the saved profile.

> 💡 **Tip**:  When your app runs in tvOS 15 or earlier, where [`shouldStorePreferencesForCurrentUser`](tvusermanager/shouldstorepreferencesforcurrentuser.md) isn’t available, display the profile picker at the beginning of each session.

 When your app runs in tvOS 15 or earlier, where [`shouldStorePreferencesForCurrentUser`](tvusermanager/shouldstorepreferencesforcurrentuser.md) isn’t available, display the profile picker at the beginning of each session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/shouldstorepreferencesforcurrentuser)*