# TVAppProfileDescriptor

**Framework**: TV Services  
**Kind**: class  
**Role**: Class

A model object that you use to represent an app-specific profile.

**Availability**:
- tvOS 13.0+ - Deprecated in 16.0

> **Deprecated**: Manually mapping profiles is deprecated. To opt-in to the system’s automatic user-data management, add the [`User Management Entitlement`](../BundleResources/entitlements/com.apple.developer.user-management.md) to your target, with a value of `runs-as-current-user-with-user-independent-keychain`. For more information, see [Mapping Apple TV users to app profiles](./mapping-apple-tv-users-to-app-profiles.md).

## Declaration

```swift
class TVAppProfileDescriptor
```

```objc
@interface TVAppProfileDescriptor : NSObject
```

#### Overview

A [`TVAppProfileDescriptor`](./tvappprofiledescriptor.md) object represents a single user profile in your app. You create app profile descriptor objects yourself and manage them in your app’s data structures. The default object contains only the user-visible name for the profile, which must be a nonempty string. You can also subclass to add app-specific properties. For example, you might add an app-specific identifier for the profile. You might also store the identifiers for all Apple TV users that are configured to use this profile.

For more information about mapping your app profiles to Apple TV accounts, see [`TVUserManager`](./tvusermanager.md).

## Topics

### Creating a Profile Descriptor
- [init(name: String)](./tvappprofiledescriptor/init%28name%29.md)
  Creates a new app profile descriptor object with the specified name.
### Getting the Profile Name
- [var name: String](./tvappprofiledescriptor/name.md)
  The user-visible label associated with the app profile.
### Initializers
- [init?(coder: NSCoder)](./tvappprofiledescriptor/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Deprecated symbols
- [var currentUserIdentifier: TVUserIdentifier?](./tvusermanager/currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](./tvusermanager/currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](./tvusermanager/presentprofilepreferencepanel%28currentsettings,availableprofiles,completion%29.md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](./tvusermanager/shouldstorepreferenceforcurrentuser%28to,completion%29.md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [typealias TVUserIdentifier](./tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](./tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvappprofiledescriptor)*