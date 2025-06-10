# autoupdatingCurrent

**Framework**: Foundation  
**Kind**: property

A locale which tracks the user’s current preferences.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var autoupdatingCurrent: Locale { get }
```

#### Discussion

This value represents the locale currently used by the app, based on the following:

- The current system locale.
- Any app-specific locale choice made in the Settings app.
- The availability of the preferred locale in the app. For example, if the person using an app has set their device to use a Spanish-language locale, but the app only supports English, this value returns an English locale.

Use this property when you want a locale that always reflects the latest configuration settings. When the person using the app changes settings, reading properties from a locale instance obtained from this property provides the latest values. If you need to rely on a locale that does not change, use the locale given by the [`current`](nslocale/current.md) property instead.

Although the locale obtained here automatically follows the latest region settings, it provides no indication when the settings change. To receive notification of locale changes, add your object as an observer of [`currentLocaleDidChangeNotification`](nslocale/currentlocaledidchangenotification.md).

## See Also

- [class var current: Locale](nslocale/current.md)
  A locale that represents the user’s region settings at the time the property is read.
- [class let currentLocaleDidChangeNotification: NSNotification.Name](nslocale/currentlocaledidchangenotification.md)
  A notification that indicates that the user’s locale changed.
- [class var system: Locale](nslocale/system.md)
  A locale representing the generic root values with little localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/autoupdatingcurrent)*