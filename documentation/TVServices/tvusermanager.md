# TVUserManager

**Framework**: TV Services  
**Kind**: class

An object that indicates how to store preferences for multiple people on a shared device.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVUserManager
```

#### Overview

Some apps rely on profiles to maintain separate information for each person who uses a shared device, such as a video content app that retains which shows they watch. To avoid interrupting people with a profile picker each time they launch your app, you can save and retrieve the current user’s selection on a shared device.

> ❗ **Important**:  To create a [`TVUserManager`](tvusermanager.md) object, add the [`User Management Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.user-management) capability to your app or app extension in Xcode, and select the Runs as Current User, Only When User-Independent Keychain is Available option. This enables the system to take care of separating each user’s data for your app.

To determine the current user’s profile, first check [`shouldStorePreferencesForCurrentUser`](tvusermanager/shouldstorepreferencesforcurrentuser.md). If that value is [`false`](https://developer.apple.com/documentation/swift/false), display the profile picker to determine which profile to use for the current session, but don’t save the selected profile. If the value is [`true`](https://developer.apple.com/documentation/swift/true), and there isn’t a saved profile in [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults), display the profile picker and save the selected profile for future use. If the value is [`true`](https://developer.apple.com/documentation/swift/true) and there’s already a saved profile, skip the prompt and use the saved profile.

## Topics

### Retaining profile selection for the current Apple TV account
- [var shouldStorePreferencesForCurrentUser: Bool](tvusermanager/shouldstorepreferencesforcurrentuser.md)
  A Boolean value that indicates whether your app needs to retain a selected profile.
### Deprecated symbols
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
- [var userIdentifiersForCurrentProfile: [TVUserIdentifier]](tvusermanager/useridentifiersforcurrentprofile.md)
  An array of system user identifiers that you associated with the current app-specific profile.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Personalizing Your App for Each User on Apple TV](personalizing-your-app-for-each-user-on-apple-tv.md)
  Use account-specific storage to segregate data on a multiuser system.
- [Supporting Multiple Users in Your tvOS App](supporting-multiple-users-in-your-tvos-app.md)
  Store separate data for each user with the new Runs as Current User capability.
- [Mapping Apple TV users to app profiles](mapping-apple-tv-users-to-app-profiles.md)
  Adapt the content of your app for the current viewer by using an entitlement and simplifying sign-in flows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvusermanager)*