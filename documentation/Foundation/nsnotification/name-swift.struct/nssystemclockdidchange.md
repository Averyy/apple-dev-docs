# NSSystemClockDidChange

**Framework**: Foundation  
**Kind**: property

A notification posted whenever the system clock is changed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let NSSystemClockDidChange: NSNotification.Name
```

#### Discussion

This can be initiated by a call to `settimeofday(_:_:)` or the user changing values in the Date and Time Preference panel.

The notification object is `null`. This notification does not contain a `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nssystemclockdidchange)*