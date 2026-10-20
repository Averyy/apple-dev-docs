# User Management Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The entitlement for distinguishing between multiple user accounts on Apple TV.

**Availability**:
- tvOS 13.0+

## Details

- **Name**: `com.apple.developer.user-management` (User Management)
- **Type**: array of string 

## Possible Values

- `get-current-user`: The value that grants access to [`TVUserManager`](../../TVServices/tvusermanager.md), so you can map your own profiles to users in the system. This value is deprecated in tvOS 16 and later. Use `runs-as-current-user-with-user-independent-keychain` instead.
- `runs-as-current-user`: The value that grants access to a separate set of data for your app for each user from GameCenter, iCloud, and local storage. Available in tvOS 14 or later. If you only want to run  as the current user on tvOS 16 or later, use `runs-as-current-user-with-user-independent-keychain` instead.
- `runs-as-current-user-with-user-independent-keychain`: The value that grants access to a separate set of data for your app for the current user. Available in tvOS 16 or later.

#### Discussion

To configure the entitlement, add the User Management capability on your app’s target in Xcode and select the checkbox for each privilege your app requires. For more details about adding a capability, see [Adding capabilities to your app](../../Xcode/adding-capabilities-to-your-app.md).

For guidance on choosing a data management strategy for your app, see [Personalizing Your App for Each User on Apple TV](../../TVServices/personalizing-your-app-for-each-user-on-apple-tv.md). For an example of how to use this entitlement in your tvOS app, see [Mapping Apple TV users to app profiles](../../TVServices/mapping-apple-tv-users-to-app-profiles.md).

> **Note**:  You can enable `runs-as-current-user` if your app’s minimum version is earlier than tvOS 14, but the app will behave as if the privilege isn’t set when running on the earlier version.

## See Also

### TV
- [com.apple.developer.video-subscriber-single-sign-on](./com.apple.developer.video-subscriber-single-sign-on.md)
  A Boolean value that indicates whether your app can use the TV Provider Authentication service.
- [com.apple.smoot.subscriptionservice](./com.apple.smoot.subscriptionservice.md)
  A Boolean value that indicates whether your app meets the requirements of the video-partner program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.user-management)*