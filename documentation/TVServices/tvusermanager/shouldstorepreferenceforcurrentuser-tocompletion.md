# shouldStorePreferenceForCurrentUser(to:completion:)

**Framework**: TV Services  
**Kind**: method

Prompts the user to save the specified profile as the preferred profile for the current user.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
func shouldStorePreferenceForCurrentUser(to profile: TVAppProfileDescriptor) async -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func shouldStorePreferenceForCurrentUser(to profile: TVAppProfileDescriptor) async -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func shouldStorePreferenceForCurrentUser(to profile: TVAppProfileDescriptor) async -> Bool
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to confirm that the profile chosen by the user should become their new preferred profile. The method prompts the user to confirm the profile change and calls the completion handler with the results. Call this method only once for each user.

## Parameters

- `profile`: The profile to associate with the current user.
- `completion`: The completion handler to call with the results. This handler has no return value and takes the following parameter:

## See Also

- [var currentUserIdentifier: TVUserIdentifier?](tvusermanager/currentuseridentifier.md)
  A unique identifier representing the currently active Apple TV user.
- [class let currentUserIdentifierDidChangeNotification: NSNotification.Name](tvusermanager/currentuseridentifierdidchangenotification.md)
  The notification the system sends when a different user becomes current.
- [func presentProfilePreferencePanel(currentSettings: [TVUserIdentifier : TVAppProfileDescriptor], availableProfiles: [TVAppProfileDescriptor], completion: ([TVUserIdentifier : TVAppProfileDescriptor]) -> Void)](tvusermanager/presentprofilepreferencepanel(currentsettings:availableprofiles:completion:).md)
  Presents a user-to-profile configuration panel, which lets the user specify their preferred profile.
- [class TVAppProfileDescriptor](tvappprofiledescriptor.md)
  A model object that you use to represent an app-specific profile.
- [typealias TVUserIdentifier](tvuseridentifier.md)
  A unique string for differentiating between accounts on Apple TV.
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager/shouldstorepreferenceforcurrentuser(to:completion:))*