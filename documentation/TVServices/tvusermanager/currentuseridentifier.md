# currentUserIdentifier

**Framework**: TV Services  
**Kind**: property

A unique identifier representing the currently active Apple TV user.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
var currentUserIdentifier: TVUserIdentifier? { get }
```

#### Discussion

Use this property to identify which Apple TV user is currently active. On Apple TV, users may provide credentials for multiple Apple accounts and switch quickly between them. This property uniquely identifies the user for the active account. You might use this information to select an appropriate user profile for your app.

The string in this property is randomly generated, and isn’t the same as the user’s Apple ID. Don’t display the string to your users. All Apple TVs on the user’s HomeKit network return the same string for the same account.

You can track changes to this property using key-value observing. You may access this property from an app extension.

## See Also

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
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/currentuseridentifier)*