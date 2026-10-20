# AppIntentError.PermissionRequired

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

Errors that indicate the app doesn’t have the required permission to perform an action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum PermissionRequired
```

#### Overview

Use these permission errors to inform people that the app requires specific permissions and that they need to grant permission to successfully complete the action.

## Topics

### Type Properties
- [static let bluetooth: AppIntentError](./permissionrequired/bluetooth.md)
  The person needs to allow the app to access to Bluetooth.
- [static let contacts: AppIntentError](./permissionrequired/contacts.md)
  The person needs to allow the app to access contacts.
- [static let localNetwork: AppIntentError](./permissionrequired/localnetwork.md)
  The person needs to allow the app to access the local network.
- [static let photos: AppIntentError](./permissionrequired/photos.md)
  The person needs to allow the app to access to the photo library.
- [static let siri: AppIntentError](./permissionrequired/siri.md)
  The person needs to allow the app to access Siri.
### Type Methods
- [static func location(precise: Bool) -> AppIntentError](./permissionrequired/location%28precise%29.md)
  The person needs to allow the app to access their location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintenterror/permissionrequired)*