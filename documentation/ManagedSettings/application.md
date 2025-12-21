# Application

**Framework**: ManagedSettings  
**Kind**: struct

A representation of an application on the user’s device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Application
```

#### Overview

Managed Settings represents apps with tokens to preserve user privacy and control.

## Topics

### Creating an Application
- [init(bundleIdentifier: String)](application/init(bundleidentifier:).md)
  Creates an object that represents the app with the specified bundle identifier.
- [init(token: ApplicationToken)](application/init(token:).md)
  Creates an object that represents the app with the specified token.
### Accessing Application Information
- [let bundleIdentifier: String?](application/bundleidentifier.md)
  The unique string that identifies this app.
- [let token: ApplicationToken?](application/token.md)
  An opaque representation of a specific web domain.
- [let localizedDisplayName: String?](application/localizeddisplayname.md)
  A localized display name for the application.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [typealias ApplicationToken](applicationtoken.md)
  A representation of an application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/application)*