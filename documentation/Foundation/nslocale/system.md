# system

**Framework**: Foundation  
**Kind**: property

A locale representing the generic root values with little localization.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var system: Locale { get }
```

#### Return Value

The generic locale that contains fixed “backstop” settings that provide values for otherwise undefined keys.

#### Discussion

Use the system locale when you don’t want any localizations. If you want localizations that match the user’s region settings, use the locale given by the [`current`](nslocale/current.md) or the [`autoupdatingCurrent`](nslocale/autoupdatingcurrent.md) property instead.

## See Also

- [class var autoupdatingCurrent: Locale](nslocale/autoupdatingcurrent.md)
  A locale which tracks the user’s current preferences.
- [class var current: Locale](nslocale/current.md)
  A locale that represents the user’s region settings at the time the property is read.
- [class let currentLocaleDidChangeNotification: NSNotification.Name](nslocale/currentlocaledidchangenotification.md)
  A notification that indicates that the user’s locale changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/system)*