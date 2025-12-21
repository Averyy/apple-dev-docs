# init(suiteName:)

**Framework**: Foundation  
**Kind**: init

Creates a new defaults object and initializes it with the settings from the specified database.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(suiteName suitename: String?)
```

#### Discussion

Use this method to create a defaults object that reads settings from the custom domain you specify. For example, you might use this method to access settings you share among multiple apps or between your app and an app extension. The returned object writes settings to the domain you specified. Every instance of ``UserDefaults shares the contents of the argument and registration domains.

The `suiteName` parameter matches the domain parameter of the corresponding CFPreferences APIs, except when translating between Foundation and Core Foundation constants. The following example shows two equivalent statements. For more details, see [`Preferences Utilities`](https://developer.apple.com/documentation/CoreFoundation/preferences-utilities).

Equivalent statements using NSUserDefaults and CFPreferences APIs

In macOS, specify another app’s bundle identifier to search that app’s settings. You can’t search another app’s settings if either app runs in an [`App Sandbox`](https://developer.apple.com/documentation/Security/app-sandbox) and you don’t have the proper entitlements.

## Parameters

- `suitename`: The name of the app group or suite to add to the search list. To read   and write settings for a shared app group, specify the app group identifier. Don’t   specify the   or your app’s bundle identifier. If you specify  ,   this method returns a defaults object that reads and writes from the current app’s settings.

## See Also

- [class var standard: UserDefaults](userdefaults/standard.md)
  The shared defaults object for the current app.
- [convenience init()](userdefaults/init.md)
  Creates a new defaults object and initializes it with the app’s current settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/init(suitename:))*