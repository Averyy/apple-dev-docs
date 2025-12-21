# removeAppExtensionPoint(_:)

**Framework**: ExtensionFoundation  
**Kind**: method

Removes the specified extension point and stops tracking the associated app extensions.

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
final func removeAppExtensionPoint(_ appExtensionPoint: AppExtensionPoint) async throws
```

#### Discussion

This method updates the state of the monitor, removing the specified extension point from the list of those it’s tracking. Removing an extension point causes the monitor to update the [`identities`](appextensionpoint/monitor/identities.md) property as needed.

## Parameters

- `appExtensionPoint`: An extension point that you define in your host app. If the   monitor isn’t currently monitoring the extension point, calling this method has no impact.

## See Also

- [func addAppExtensionPoint(AppExtensionPoint) async throws](appextensionpoint/monitor/addappextensionpoint(_:).md)
  Begins the tracking of app extensions that support the specified extension point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/removeappextensionpoint(_:))*