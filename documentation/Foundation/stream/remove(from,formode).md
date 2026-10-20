# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the receiver from a given run loop running in a given mode.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) removeFromRunLoop:(NSRunLoop *) aRunLoop forMode:(NSRunLoopMode) mode;
```

## Parameters

- `aRunLoop`: The run loop on which the receiver was scheduled.
- `mode`: The mode for the run loop.

## See Also

### Managing Run Loops
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](./schedule%28in,formode%29.md)
  Schedules the receiver on a given run loop in a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/remove(from:formode:))*