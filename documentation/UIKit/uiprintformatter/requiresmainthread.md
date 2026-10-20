# requiresMainThread

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL requiresMainThread;
```

#### Discussion

The default value is [`true`](../../Swift/true.md), which requires the printing system to execute rendering operations, like drawing and page-count calculation, on the main thread. Override this property to return [`false`](../../Swift/false.md) if you want the system to execute operations like [`draw(in:forPageAt:)`](./draw%28in,forpageat%29.md) and [`pageCount`](./pagecount.md) on a background thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/requiresmainthread)*