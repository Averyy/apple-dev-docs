# presentProfilePreferencePanel(currentSettings:availableProfiles:completion:)

**Framework**: TV Services  
**Kind**: method  
**Role**: Instance Method

Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.

**Availability**:
- tvOS 13.0+ - Deprecated in 16.0

> **Deprecated**: Manually mapping profiles is deprecated. To opt-in to the system’s automatic user-data management, add the [`User Management Entitlement`](../../BundleResources/entitlements/com.apple.developer.user-management.md) to your target, with a value of `runs-as-current-user-with-user-independent-keychain`. For more information, see [Mapping Apple TV users to app profiles](../mapping-apple-tv-users-to-app-profiles.md).

## Declaration

```swift
func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: @escaping @Sendable ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)
```

```swift
func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor]) async -> [TVUserIdentifier : TVAppProfileDescriptor]
```

```objc
- (void) presentProfilePreferencePanelWithCurrentSettings:(NSDictionary<NSString *,TVAppProfileDescriptor *> *) currentSettings availableProfiles:(NSArray<TVAppProfileDescriptor *> *) availableProfiles completion:(void (^)(NSDictionary<NSString *,TVAppProfileDescriptor *> *newSettings)) completion;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor]) async -> [TVUserIdentifier : TVAppProfileDescriptor]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Calling this method displays a panel that lets the user configure which app-specific profile to associate with each Apple TV user account. The panel gives the user the option to select from any of the profiles in the `availableProfiles` parameter. It also uses the information in the `existingSettings` parameter to configure the initial mapping between users and profiles. After configuring the user accounts and dismissing the panel, the system calls your `completion` handler to deliver the updated mapping between user accounts and profiles.

## Parameters

- `availableProfiles`: The complete list of app-specific profiles available in your app. The configuration panel displays this set of profiles to the user.
- `completion`: The completion handler to call when the user dismisses the configuration panel. This handler has no return value and takes the following parameter:

  - **newSettings**: A dictionary containing an updated map from system user to app profile. The information is similar to what you provide in the `existingSettings` parameter, but reflects the changes made by the user.

## See Also

### Deprecated symbols
- [var currentUserIdentifier: TVUserIdentifier?](./currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](./currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](./shouldstorepreferenceforcurrentuser%28to,completion%29.md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [class TVAppProfileDescriptor](../tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](../tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](./useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/presentprofilepreferencepanel(currentsettings:availableprofiles:completion:))*