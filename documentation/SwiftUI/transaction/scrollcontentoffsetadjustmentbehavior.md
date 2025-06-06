# scrollContentOffsetAdjustmentBehavior

**Framework**: SwiftUI  
**Kind**: property

The behavior a scroll view will have regarding content offset adjustments for the current transaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var scrollContentOffsetAdjustmentBehavior: ScrollContentOffsetAdjustmentBehavior { get set }
```

#### Discussion

A scroll view may automatically adjust its content offset based on the current context. The absolute offset may be adjusted to keep content in relatively the same place. For example, when scrolled to the bottom, a scroll view may keep the bottom edge scrolled to the bottom when the overall size of its content changes.

Use this property to disable these kinds of adjustments when needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transaction/scrollcontentoffsetadjustmentbehavior)*