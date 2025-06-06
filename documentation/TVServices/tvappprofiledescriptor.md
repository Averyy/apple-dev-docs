# TVAppProfileDescriptor

**Framework**: TV Services  
**Kind**: class

A model object that you use to represent an app-specific profile.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVAppProfileDescriptor
```

#### Overview

A [`TVAppProfileDescriptor`](tvappprofiledescriptor.md) object represents a single user profile in your app. You create app profile descriptor objects yourself and manage them in your app’s data structures. The default object contains only the user-visible name for the profile, which must be a nonempty string. You can also subclass to add app-specific properties. For example, you might add an app-specific identifier for the profile. You might also store the identifiers for all Apple TV users that are configured to use this profile.

For more information about mapping your app profiles to Apple TV accounts, see [`TVUserManager`](tvusermanager.md).

## Topics

### Creating a Profile Descriptor
- [init(name: String)](tvappprofiledescriptor/init(name:).md)
  Creates a new app profile descriptor object with the specified name.
### Getting the Profile Name
- [var name: String](tvappprofiledescriptor/name.md)
  The user-visible label associated with the app profile.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [var currentUserIdentifier: TVUserIdentifier?](tvusermanager/currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](tvusermanager/currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](tvusermanager/presentprofilepreferencepanel(currentsettings:availableprofiles:completion:).md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](tvusermanager/shouldstorepreferenceforcurrentuser(to:completion:).md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [typealias TVUserIdentifier](tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvappprofiledescriptor)*