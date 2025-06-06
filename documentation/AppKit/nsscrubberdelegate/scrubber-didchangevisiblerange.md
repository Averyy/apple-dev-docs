# scrubber(_:didChangeVisibleRange:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the range of items currently visible in the scrubber has changed.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func scrubber(_ scrubber: NSScrubber, didChangeVisibleRange visibleRange: NSRange)
```

## Parameters

- `scrubber`: The scrubber object that is notifying you of the change in the range of items that are currently visible.
- `visibleRange`: The range of items that are now visible in the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubberdelegate/scrubber(_:didchangevisiblerange:))*