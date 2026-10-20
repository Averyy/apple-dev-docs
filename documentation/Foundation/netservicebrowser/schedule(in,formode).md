# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds the receiver to the specified run loop.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_browser_t in Network framework instead

## Declaration

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) scheduleInRunLoop:(NSRunLoop *) aRunLoop forMode:(NSRunLoopMode) mode;
```

#### Discussion

You can use this method in conjunction with [`remove(from:forMode:)`](./remove%28from,formode%29.md) to transfer the receiver to a run loop other than the default one. You should not attempt to run the receiver on multiple run loops.

## Parameters

- `aRunLoop`: Run loop in which to schedule the receiver.
- `mode`: Run loop mode in which to perform this operation, such as [`default`](../runloop/mode/default.md). See the Run Loop Modes section of the [`RunLoop`](../runloop.md) class for other run loop mode values.

## See Also

### Managing Run Loops
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](./remove%28from,formode%29.md)
  Removes the receiver from the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/schedule(in:formode:))*