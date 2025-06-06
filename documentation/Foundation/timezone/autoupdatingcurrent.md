# autoupdatingCurrent

**Framework**: Foundation  
**Kind**: property

The time zone currently used by the system, automatically updating to the user’s current preference.

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
static var autoupdatingCurrent: TimeZone { get }
```

#### Discussion

If this time zone is mutated, then it no longer tracks the system time zone.

The autoupdating time zone only compares equal to itself.

## See Also

- [static var current: TimeZone](timezone/current.md)
  The time zone currently used by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/timezone/autoupdatingcurrent)*