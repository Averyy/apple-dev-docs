# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the receiver from the specified run loop.

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
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) removeFromRunLoop:(NSRunLoop *) aRunLoop forMode:(NSRunLoopMode) mode;
```

#### Discussion

You can use this method in conjunction with [`schedule(in:forMode:)`](./schedule%28in,formode%29.md) to transfer the receiver to a run loop other than the default one. Although it is possible to remove an `NSNetService` object completely from any run loop and then attempt actions on it, you must not do it.

## Parameters

- `aRunLoop`: Run loop from which to remove the receiver.
- `mode`: Run loop mode in which to perform this operation, such as [`default`](../runloop/mode/default.md). See the Run Loop Modes section of the [`RunLoop`](../runloop.md) class for other run loop mode values.

## See Also

### Managing Run Loops
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](./schedule%28in,formode%29.md)
  Adds the receiver to the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicebrowser/remove(from:formode:))*