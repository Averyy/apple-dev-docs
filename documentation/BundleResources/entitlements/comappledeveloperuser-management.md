# User Management Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement for distinguishing between multiple user accounts on Apple TV.

**Availability**:
- tvOS 13.0+

#### Discussion

To configure the entitlement, add the User Management capability on your app’s target in Xcode and select the checkbox for each privilege your app requires. For more details about adding a capability, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app).

For guidance on choosing a data management strategy for your app, see [`Personalizing Your App for Each User on Apple TV`](https://developer.apple.com/documentation/TVServices/personalizing-your-app-for-each-user-on-apple-tv). For an example of how to use this entitlement in your tvOS app, see [`Mapping Apple TV users to app profiles`](https://developer.apple.com/documentation/TVServices/mapping-apple-tv-users-to-app-profiles).

> **Note**:  You can enable `runs-as-current-user` if your app’s minimum version is earlier than tvOS 14, but the app will behave as if the privilege isn’t set when running on the earlier version.

## See Also

- [com.apple.developer.video-subscriber-single-sign-on](entitlements/com.apple.developer.video-subscriber-single-sign-on.md)
  A Boolean value that indicates whether your app can use the TV Provider Authentication service.
- [com.apple.smoot.subscriptionservice](entitlements/com.apple.smoot.subscriptionservice.md)
  A Boolean value that indicates whether your app can integrate with APIs to provide different feed based content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.user-management)*