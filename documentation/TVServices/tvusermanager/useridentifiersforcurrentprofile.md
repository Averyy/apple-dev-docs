# userIdentifiersForCurrentProfile

**Framework**: TV Services  
**Kind**: property  
**Role**: Instance Property

An array of system user identifiers that you associated with the current app-specific profile.

**Availability**:
- tvOS 13.0+ - Deprecated in 16.0

> **Deprecated**: Manually mapping profiles is deprecated. To opt-in to the system’s automatic user-data management, add the [`User Management Entitlement`](../../BundleResources/entitlements/com.apple.developer.user-management.md) to your target, with a value of `runs-as-current-user-with-user-independent-keychain`. For more information, see [Mapping Apple TV users to app profiles](../mapping-apple-tv-users-to-app-profiles.md).

## Declaration

```swift
var userIdentifiersForCurrentProfile: [TVUserIdentifier] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * userIdentifiersForCurrentProfile;
```

## Discussion

If your app remembers which app-specific profile each Apple TV user prefers, use this property to provide that information to the system. Fill this property with zero or more user identifiers that you previously retrieved from the [`currentUserIdentifier`](./currentuseridentifier.md) property. Doing so creates a mapping between your app profiles and the Apple TV accounts that prefer them. The system uses the information in this property to provide better information in user dialogs and doesn’t change the property’s value.

Update this property whenever the user selects a different app profile. The system doesn’t change the value in this property, so it contains the last value that you assigned to it since app launch. However, the property supports key-value observing if you want to track the changes that you make from other parts of your app.

## See Also

### Deprecated symbols
- [var currentUserIdentifier: TVUserIdentifier?](./currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](./currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](./presentprofilepreferencepanel%28currentsettings,availableprofiles,completion%29.md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](./shouldstorepreferenceforcurrentuser%28to,completion%29.md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [class TVAppProfileDescriptor](../tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](../tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/useridentifiersforcurrentprofile)*