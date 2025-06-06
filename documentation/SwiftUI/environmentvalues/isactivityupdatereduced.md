# isActivityUpdateReduced

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether the Live Activity update synchronization rate is reduced.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var isActivityUpdateReduced: Bool { get set }
```

#### Discussion

When rendering an Activity on a remote device such as Apple Watch, content updates may sometimes be limited to only alerting updates, depending on system conditions. When a live activity is being shown and only alerting updates are being synchronized to the remote device, the value of `isActivityUpdateReduced` will be `true`.

For example, `isActivityUpdateReduced` may be `true` for Live Activities displayed on watchOS when out of range of the paired iPhone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isactivityupdatereduced)*