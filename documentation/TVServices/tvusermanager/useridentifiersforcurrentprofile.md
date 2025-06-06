# userIdentifiersForCurrentProfile

**Framework**: TV Services  
**Kind**: property

An array of system user identifiers that you associated with the current app-specific profile.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var userIdentifiersForCurrentProfile: [TVUserIdentifier] { get set }
```

#### Discussion

If your app remembers which app-specific profile each Apple TV user prefers, use this property to provide that information to the system. Fill this property with zero or more user identifiers that you previously retrieved from the [`currentUserIdentifier`](tvusermanager/currentuseridentifier.md) property. Doing so creates a mapping between your app profiles and the Apple TV accounts that prefer them. The system uses the information in this property to provide better information in user dialogs and doesn’t change the property’s value.

Update this property whenever the user selects a different app profile. The system doesn’t change the value in this property, so it contains the last value that you assigned to it since app launch. However, the property supports key-value observing if you want to track the changes that you make from other parts of your app.

## See Also

- [var currentUserIdentifier: TVUserIdentifier?](tvusermanager/currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](tvusermanager/currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](tvusermanager/presentprofilepreferencepanel(currentsettings:availableprofiles:completion:).md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](tvusermanager/shouldstorepreferenceforcurrentuser(to:completion:).md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [class TVAppProfileDescriptor](tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/useridentifiersforcurrentprofile)*