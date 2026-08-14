# RequestAppDeletionAction

**Framework**: MarketplaceKit  
**Kind**: struct

A SwiftUI environment action that requests the deletion of an app.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
struct RequestAppDeletionAction
```

#### Overview

Use this action in SwiftUI views to request app deletion. The system presents a confirmation to ensure that the person approves the app’s deletion.

## Topics

### Making a request
- [func callAsFunction(AppLibrary.App) async throws](requestappdeletionaction/callasfunction(_:).md)
  Requests deletion of the specified app with someone’s confirmation.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AppLibrary](applibrary.md)
  A class that represents a catalog of all installed apps, and offers various services for the apps that your marketplace distributes.
- [struct AppVersion](appversion.md)
  Information that describes an app, including its identifier and version number.
- [struct AutomaticUpdate](automaticupdate.md)
  Information that describes an app that’s available for update, including a download URL.
- [struct InstallRequirements](installrequirements.md)
  An app’s installation criteria for a device.
- [typealias AppleItemID](appleitemid.md)
  An identifier that represents an app.
- [typealias AppleVersionID](appleversionid.md)
  An identifier that represents a single app version.
- [let MarketplaceKitURIScheme: String](marketplacekiturischeme.md)
  A URI scheme that defines an alternative distribution app installation link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/requestappdeletionaction)*