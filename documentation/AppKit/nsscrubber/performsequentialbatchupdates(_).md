# performSequentialBatchUpdates(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Combines multiple scrubber content updates into a single action.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
func performSequentialBatchUpdates(_ updateBlock: () -> Void)
```

```objc
- (void) performSequentialBatchUpdates:(void (^)()) updateBlock;
```

## Parameters

- `updateBlock`: A block that represents the combination of insertion, removal, moving, and reloading instructions that should be performed simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/performsequentialbatchupdates(_:))*