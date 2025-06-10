# autoupdatingCurrent

**Framework**: Foundation  
**Kind**: property

A locale which tracks the user’s current preferences.

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
static var autoupdatingCurrent: Locale { get }
```

#### Discussion

This value represents the locale currently used by the app, based on the following:

- The current system locale.
- Any app-specific locale choice made in the Settings app.
- The availability of the preferred locale in the app. For example, if the person using an app has set their device to use a Spanish-language locale, but the app only supports English, this value returns an English locale.

Use this property when you want a locale that always reflects the latest configuration settings. When the person using the app changes settings, reading properties from a locale instance obtained from this property provides the latest values. If you need to rely on a locale that does not change, use the locale given by the [`current`](locale/current.md) property instead.

Although the locale obtained here automatically follows the latest language and region settings, it provides no indication when the settings change. To receive notification of locale changes in Swift, add an observer for [`Locale.CurrentLocaleDidChangeMessage`](locale/currentlocaledidchangemessage.md). In Objective-C, you can add your object as an observer of `NSCurrentLocaleDidChangeNotification`.

If mutated, this `Locale` no longer tracks the user’s preferences.

> **Note**:  The autoupdating `Locale` only compares as equal to another autoupdating `Locale`.

## See Also

- [static var current: Locale](locale/current.md)
  A locale representing the user’s region settings at the time the property is read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/autoupdatingcurrent)*