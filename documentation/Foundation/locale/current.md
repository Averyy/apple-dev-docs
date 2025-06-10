# current

**Framework**: Foundation  
**Kind**: property

A locale representing the user’s region settings at the time the property is read.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var current: Locale { get }
```

#### Discussion

This value represents the locale currently used by the app, based on the following:

- The current system locale.
- Any app-specific locale choice made in the Settings app.
- The availability of the preferred locale in the app. For example, if the person using an app has set their device to use a Spanish-language locale, but the app only supports English, this value returns an English locale.

Use this property when you need to rely on a consistent locale. A locale instance obtained this way does not change even when the person using the device changes language or region settings. If you want a locale instance that always reflects the current configuration, use the one provided by the [`autoupdatingCurrent`](locale/autoupdatingcurrent.md) property instead.

To receive notification of locale changes in Swift, add an observer for [`Locale.CurrentLocaleDidChangeMessage`](locale/currentlocaledidchangemessage.md). In Objective-C, you can add your object as an observer of [`currentLocaleDidChangeNotification`](nslocale/currentlocaledidchangenotification.md).

## See Also

- [static var autoupdatingCurrent: Locale](locale/autoupdatingcurrent.md)
  A locale which tracks the user’s current preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/current)*