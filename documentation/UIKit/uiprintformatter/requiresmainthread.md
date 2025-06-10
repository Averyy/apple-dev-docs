# requiresMainThread

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the system executes the print formatter’s rendering operations on the main thread.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var requiresMainThread: Bool { get }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true), which requires the printing system to execute rendering operations, like drawing and page-count calculation, on the main thread. Override this property to return [`false`](https://developer.apple.com/documentation/swift/false) if you want the system to execute operations like [`draw(in:forPageAt:)`](uiprintformatter/draw(in:forpageat:).md) and [`pageCount`](uiprintformatter/pagecount.md) on a background thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/requiresmainthread)*