# currentUserIdentifierDidChangeNotification

**Framework**: TV Services  
**Kind**: property  
**Role**: Type Property

The notification the system sends when a different user becomes current.

**Availability**:
- tvOS 13.0+ - Deprecated in 16.0

> **Deprecated**: Manually mapping profiles is deprecated. To opt-in to the system’s automatic user-data management, add the [`User Management Entitlement`](../../BundleResources/entitlements/com.apple.developer.user-management.md) to your target, with a value of `runs-as-current-user-with-user-independent-keychain`. For more information, see [Mapping Apple TV users to app profiles](../mapping-apple-tv-users-to-app-profiles.md).

## Declaration

```swift
class let currentUserIdentifierDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const TVUserManagerCurrentUserIdentifierDidChangeNotification;
```

#### Discussion

The object of the notification is `nil`. The notification doesn’t add any keys to the [`userInfo`](../../Foundation/nsnotification/userinfo.md) dictionary.

## See Also

### Deprecated symbols
- [var currentUserIdentifier: TVUserIdentifier?](./currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](./presentprofilepreferencepanel%28currentsettings,availableprofiles,completion%29.md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](./shouldstorepreferenceforcurrentuser%28to,completion%29.md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [class TVAppProfileDescriptor](../tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](../tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](./useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/currentuseridentifierdidchangenotification)*