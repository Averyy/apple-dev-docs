# AppLock.App

**Framework**: Device Management  
**Kind**: dictionary

The only app available for use on the iOS device.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- tvOS 10.2+

## Declaration

```swift
object AppLock.App
```

## Topics

### Objects
- [object AppLock.App.Options](applock/app-data.dictionary/options-data.dictionary.md)
  The dictionary of options to set for the app.
- [object AppLock.App.UserEnabledOptions](applock/app-data.dictionary/userenabledoptions-data.dictionary.md)
  The dictionary of user-editable options to set for the app.

## Properties

- `Identifier` (string) *(required)*: The app’s bundle identifier.
- `Options` (AppLock.App.Options): A dictionary of options that the user can’t change. Available: iOS 7+ | iPadOS 7+ | tvOS 10.2+
- `UserEnabledOptions` (AppLock.App.UserEnabledOptions): A dictionary of user-editable options. Available: iOS 7+ | iPadOS 7+ | tvOS 10.2+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/applock/app-data.dictionary)*