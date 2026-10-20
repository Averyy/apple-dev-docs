# remove(from:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the service from the given run loop for a given mode.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.2+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use nw_connection_t or nw_listener_t in Network framework instead

## Declaration

```swift
func remove(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) removeFromRunLoop:(NSRunLoop *) aRunLoop forMode:(NSRunLoopMode) mode;
```

#### Discussion

You can use this method in conjunction with [`schedule(in:forMode:)`](./schedule%28in,formode%29.md) to transfer the service to a different run loop. Although it is possible to remove an `NSNetService` object completely from any run loop and then attempt actions on it, it is an error to do so.

## Parameters

- `aRunLoop`: The run loop from which to remove the receiver.
- `mode`: The run loop mode from which to remove the receiver. Possible values for `mode` are discussed in the “Constants” section of [`RunLoop`](../runloop.md).

## See Also

### Managing Run Loops
- [func schedule(in: RunLoop, forMode: RunLoop.Mode)](./schedule%28in,formode%29.md)
  Adds the service to the specified run loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/remove(from:formode:))*