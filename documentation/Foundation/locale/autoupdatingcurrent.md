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

If mutated, this Locale will no longer track the user’s preferences.

> **Note**:  The autoupdating Locale will only compare equal to another autoupdating Locale.

## See Also

- [static var current: Locale](locale/current.md)
  A locale representing the user’s region settings at the time the property is read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/autoupdatingcurrent)*