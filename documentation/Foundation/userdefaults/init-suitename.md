# init(suiteName:)

**Framework**: Foundation  
**Kind**: init

Creates a user defaults object initialized with the defaults for the specified database name.

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

You can use this method when developing an app suite, to share preferences or other data among the apps, or when developing an app extension, to share preferences or other data between the extension and its containing app.

The argument and registration domains are shared between all instances of [`UserDefaults`](userdefaults.md).

The `suiteName` parameter matches the domain parameter of the corresponding CFPreferences APIs (except when translating between Foundation and Core Foundation constants). The code example below shows two equivalent statements. For more details, see [`Preferences Utilities`](https://developer.apple.com/documentation/CoreFoundation/preferences-utilities).

Equivalent statements using NSUserDefaults and CFPreferences APIs

On macOS, specifying another app’s bundle identifier will get you that app’s preferences search list, unless prevented by the [`App Sandbox`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/CoreOSLayer/CoreOSLayer.html#//apple_ref/doc/uid/TP40001067-CH9-SW3).

## Parameters

- `suitename`: If you pass   to this parameter, the system uses the default search list that the   class method uses. Because a suite manages the defaults of a specified app group, a suite name must be distinct from your app’s main bundle identifier. The   is also an invalid suite name, because it isn’t writeable by apps.

## See Also

- [convenience init()](userdefaults/init.md)
  Creates a user defaults object initialized with the defaults for the app and current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/init(suitename:))*