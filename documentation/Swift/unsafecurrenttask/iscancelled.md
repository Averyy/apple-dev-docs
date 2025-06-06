# isCancelled

**Framework**: Swift  
**Kind**: property

A Boolean value that indicates whether the current task was canceled.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

#### Discussion

After the value of this property becomes `true`, it remains `true` indefinitely. There is no way to uncancel a task.

> **Note**: `checkCancellation()`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecurrenttask/iscancelled)*