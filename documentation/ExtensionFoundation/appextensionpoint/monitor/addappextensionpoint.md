# addAppExtensionPoint(_:)

**Framework**: ExtensionFoundation  
**Kind**: method

Begins the tracking of app extensions that support the specified extension point.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
final func addAppExtensionPoint(_ appExtensionPoint: AppExtensionPoint) async throws
```

## Mentions

- [Discovering app extensions from your app](discovering-app-extensions-from-your-app.md)

#### Discussion

This method updates the state of the monitor, adding the specified extension point to the list of those it’s tracking. If the new extension point has available app extensions, this method updates the contents of the [`identities`](appextensionpoint/monitor/identities.md) property.  You can call this method multiple times to track multiple extension points from your app.

## Parameters

- `appExtensionPoint`: An extension point that you define in your host app. If the   monitor is already tracking the extension point, calling this method has no impact.

## See Also

- [func removeAppExtensionPoint(AppExtensionPoint) async throws](appextensionpoint/monitor/removeappextensionpoint(_:).md)
  Removes the specified extension point and stops tracking the associated app extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/addappextensionpoint(_:))*