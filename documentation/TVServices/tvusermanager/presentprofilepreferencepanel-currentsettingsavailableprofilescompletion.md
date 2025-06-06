# presentProfilePreferencePanel(currentSettings:availableProfiles:completion:)

**Framework**: TV Services  
**Kind**: method

Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor]) async -> [TVUserIdentifier : TVAppProfileDescriptor]
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor]) async -> [TVUserIdentifier : TVAppProfileDescriptor]
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor]) async -> [TVUserIdentifier : TVAppProfileDescriptor]
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Calling this method displays a panel that lets the user configure which app-specific profile to associate with each Apple TV user account. The panel gives the user the option to select from any of the profiles in the `availableProfiles` parameter. It also uses the information in the `existingSettings` parameter to configure the initial mapping between users and profiles. After configuring the user accounts and dismissing the panel, the system calls your `completion` handler to deliver the updated mapping between user accounts and profiles.

## Parameters

- `availableProfiles`: The complete list of app-specific profiles available in your app. The configuration panel displays this set of profiles to the user.
- `completion`: The completion handler to call when the user dismisses the configuration panel. This handler has no return value and takes the following parameter:

## See Also

- [var currentUserIdentifier: TVUserIdentifier?](tvusermanager/currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](tvusermanager/currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func shouldStorePreferenceForCurrentUser(to: TVAppProfileDescriptor, completion: (Bool) -> Void)](tvusermanager/shouldstorepreferenceforcurrentuser(to:completion:).md)
  Prompts the user to save the specified profile as the preferred profile for the current user.
- [class TVAppProfileDescriptor](tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/presentprofilepreferencepanel(currentsettings:availableprofiles:completion:))*