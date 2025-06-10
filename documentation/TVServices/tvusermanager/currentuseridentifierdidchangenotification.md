# currentUserIdentifierDidChangeNotification

**Framework**: TV Services  
**Kind**: property

The notification the system sends when a different user becomes current.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class let currentUserIdentifierDidChangeNotification: NSNotification.Name
```

#### Discussion

The object of the notification is `nil`. The notification doesn’t add any keys to the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSNotification/userInfo) dictionary.

## See Also

- [var currentUserIdentifier: TVUserIdentifier?](tvusermanager/currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](tvusermanager/presentprofilepreferencepanel(currentsettings:availableprofiles:completion:).md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](tvusermanager/shouldstorepreferenceforcurrentuser(to:completion:).md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [class TVAppProfileDescriptor](tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/currentuseridentifierdidchangenotification)*