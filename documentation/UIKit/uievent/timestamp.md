# timestamp

**Framework**: UIKit  
**Kind**: property

The time when the event occurred.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var timestamp: TimeInterval { get }
```

#### Discussion

This property contains the number of seconds that have elapsed since system startup. For a description of this time value, see the description of the [`systemUptime`](https://developer.apple.com/documentation/Foundation/ProcessInfo/systemUptime) method of the [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/timestamp)*