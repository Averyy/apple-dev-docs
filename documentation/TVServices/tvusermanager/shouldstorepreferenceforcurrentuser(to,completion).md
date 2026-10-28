# shouldStorePreferenceForCurrentUser(to:completion:)

**Framework**: TV Services  
**Kind**: method  
**Role**: Instance Method

Prompts the user to save the specified profile as the preferred profile for the current user.

**Availability**:
- tvOS 13.0+ - Deprecated in 16.0

> **Deprecated**: Manually mapping profiles is deprecated. To opt-in to the system’s automatic user-data management, add the [`User Management Entitlement`](../../BundleResources/entitlements/com.apple.developer.user-management.md) to your target, with a value of `runs-as-current-user-with-user-independent-keychain`. For more information, see [Mapping Apple TV users to app profiles](../mapping-apple-tv-users-to-app-profiles.md).

## Declaration

```swift
func shouldStorePreferenceForCurrentUser(to profile: TVAppProfileDescriptor, completion: @escaping @Sendable (Bool) -> Void)
```

```swift
func shouldStorePreferenceForCurrentUser(to profile: TVAppProfileDescriptor) async -> Bool
```

```objc
- (void) shouldStorePreferenceForCurrentUserToProfile:(TVAppProfileDescriptor *) profile completion:(void (^)(BOOL shouldCreateMapping)) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func shouldStorePreferenceForCurrentUser(to profile: TVAppProfileDescriptor) async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Use this method to confirm that the profile chosen by the user should become their new preferred profile. The method prompts the user to confirm the profile change and calls the completion handler with the results. Call this method only once for each user.

## Parameters

- `profile`: The profile to associate with the current user.
- `completion`: The completion handler to call with the results. This handler has no return value and takes the following parameter:

  - **shouldCreateMapping**: A Boolean value indicating whether your app should associate the specified profile with the current user. If this parameter is [`true`](../../Swift/true.md), save the association in your app’s data structures.

## See Also

### Deprecated symbols
- [var currentUserIdentifier: TVUserIdentifier?](./currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](./currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](./presentprofilepreferencepanel%28currentsettings,availableprofiles,completion%29.md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [class TVAppProfileDescriptor](../tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](../tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](./useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/shouldstorepreferenceforcurrentuser(to:completion:))*