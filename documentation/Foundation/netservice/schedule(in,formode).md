# schedule(in:forMode:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds the service to the specified run loop.

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
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) scheduleInRunLoop:(NSRunLoop *) aRunLoop forMode:(NSRunLoopMode) mode;
```

## Discussion

You can use this method in conjunction with [`remove(from:forMode:)`](./remove%28from,formode%29.md) to transfer a service to a different run loop. You should not attempt to run a service on multiple run loops.

## Parameters

- `aRunLoop`: The run loop to which to add the receiver.
- `mode`: The run loop mode to which to add the receiver. Possible values for `mode` are discussed in the “Constants” section of [`RunLoop`](../runloop.md).

## See Also

### Managing Run Loops
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](./remove%28from,formode%29.md)
  Removes the service from the given run loop for a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservice/schedule(in:formode:))*