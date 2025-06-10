# AppIntentError.PermissionRequired

**Framework**: App Intents  
**Kind**: enum

Errors that indicate that the app doesn’t have required permission to perform an action

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum PermissionRequired
```

#### Overview

Use the permission errors to inform a person that the app requires specific permissions and that they need to grant a permission to successfully complete the action.

## Topics

### Type Properties
- [static let bluetooth: AppIntentError](appintenterror/permissionrequired/bluetooth.md)
  User needs to grant bluetooth permission to the app
- [static let contacts: AppIntentError](appintenterror/permissionrequired/contacts.md)
  User needs to grant contacts permission to the app
- [static let localNetwork: AppIntentError](appintenterror/permissionrequired/localnetwork.md)
  User needs to grant local network access to the app
- [static let photos: AppIntentError](appintenterror/permissionrequired/photos.md)
  User needs to grant photos permission to the app
- [static let siri: AppIntentError](appintenterror/permissionrequired/siri.md)
  User needs to grant Siri permission to the app
### Type Methods
- [static func location(precise: Bool) -> AppIntentError](appintenterror/permissionrequired/location(precise:).md)
  User needs to grant location permission to the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/permissionrequired)*